__author__ = 'bkoenighofer'

from datatypes.dfanode import DfaNode
from datatypes.dfa import DFA
from datatypes.dfalabel import DfaLabel
from itertools import combinations

import time

DEBUG = 0

class DfaGenerator(object):

    def __init__(self, specDfa):

        '''
        Constructor
        '''
        #original Specification Automaton
        self.specDfa_ = specDfa

    '''
    Construction of the Deviation and Correctness Monitor

    1) If the output of the system is safe, the shield has to give the same output
    2) If the output of the system is unsafe, the shield has to deviate and to give a safe one
    3) all other states are unsafe

    '''
    def buildShieldAutomaton(self):
        #build state list

        spec_dfa = self.specDfa_
        shield_dfa = DFA()
        shield_dfa.setVarNames(spec_dfa.getVarNames())

        #inputs consist of system's inputs and outputs
        shield_dfa.setInputVars(spec_dfa.getInputVars())
        shield_dfa.addInputVars(spec_dfa.getOutputVars())

        #output of shield = copies of system outputs
        for varNr in spec_dfa.getOutputVars():
            shieldVarNr = varNr + spec_dfa.getVarNum()
            shieldVarName = spec_dfa.getVarName(varNr) + "__1"
            shield_dfa.addOutputVar(shieldVarNr)
            shield_dfa.setVarName(shieldVarNr, shieldVarName)

        errorState = DfaNode(1)

        #copy nodes from spec automata
        for specState in spec_dfa.getNodes():
            state = DfaNode(specState)
            shield_dfa.addNode(state, True)
            if state.isFinal():
                errorState = state
                shield_dfa.addEdge(errorState, errorState, DfaLabel([]))

        for specState in spec_dfa.getNodes():

            #get list of all labels that lead to a safe state
            safeOptions = []
            for specEdge in specState.getOutgoingEdges():
                shieldSource = shield_dfa.getNode(specEdge.getSourceNode().getNr())
                shieldTarget = shield_dfa.getNode(specEdge.getTargetNode().getNr())

                if not shieldSource.isFinal():
                    if not shieldTarget.isFinal():
                        safeOptions.append([specEdge.getLabel(), shieldTarget])

            for specEdge in specState.getOutgoingEdges():
                shieldSource = shield_dfa.getNode(specEdge.getSourceNode().getNr())
                shieldTarget = shield_dfa.getNode(specEdge.getTargetNode().getNr())

                if not shieldSource.isFinal():
                    if not shieldTarget.isFinal():
                        specLabel = specEdge.getLabel()

                        #1a) If the output of the system is safe, the shield has to give the same output
                        systemOutVars = spec_dfa.getOutputVars()
                        for var in range(0, len(systemOutVars)+1):
                            for subset in combinations(systemOutVars, var):
                                #construct label: all vars in subset are negated
                                label = self.createLabelFromSubset(subset)
                                combLabel = label.merge(specLabel)
                                if combLabel.isValidLabel():
                                   shield_dfa.addEdge(shieldSource, shieldTarget, combLabel)

                        #1b) If the output of the system is safe, and the shield deviates, go to the error state
                        #for each output literal, if output literal of shield is different, go to error state
                        specInLiterals = spec_dfa.getInputLiterals(specLabel)
                        specOutLiterals = spec_dfa.getOutputLiterals(specLabel)
                        for outVar in spec_dfa.getOutputVars():
                            #positive literal
                            combLabel = specLabel.merge(DfaLabel([outVar]))
                            if combLabel.isValidLabel():
                                literals = specInLiterals+specOutLiterals
                                if outVar not in literals:
                                    literals.append(outVar)
                                literals.append((outVar+spec_dfa.getVarNum())*-1)
                                shield_dfa.addEdge(shieldSource, errorState, DfaLabel(literals))
                            #negative literal
                            combLabel = specLabel.merge(DfaLabel([-outVar]))
                            if combLabel.isValidLabel():
                                literals = specInLiterals+specOutLiterals
                                if -outVar not in literals:
                                    literals.append(-outVar)
                                literals.append((outVar+spec_dfa.getVarNum()))
                                shield_dfa.addEdge(shieldSource, errorState, DfaLabel(literals))

                    else:
                        #2) If the output of the system is unsafe, the shield has to deviate and to give a safe one

                        badSpecLabel = specEdge.getLabel()
                        #compute set of safe labels, that have the same system inputs
                        for safeOption in safeOptions:
                            safeLabel = safeOption[0]
                            if spec_dfa.checkInputCompatibility(safeLabel, badSpecLabel):
                                #transform spec out literals to shield out literals
                                literals = badSpecLabel.getLiterals()
                                specOutLiterals = spec_dfa.getOutputLiterals(safeLabel)
                                for specOutLit in specOutLiterals:
                                    shieldOutLit = abs(specOutLit)+spec_dfa.getVarNum()
                                    if specOutLit < 0:
                                        shieldOutLit=shieldOutLit*-1
                                    literals.append(shieldOutLit)
                                shield_dfa.addEdge(shieldSource, safeOption[1], DfaLabel(literals))

        #print("Final Shield DFA")
        #shield_dfa.debugPrintDfa(True)

        return shield_dfa.standardization()

    '''
    Computes a label from a subset

    Helper Function to build a ShieldDeviationAutomaton.
    Takes a subset of Design-Variables, e.g. o1, o3.
    All Design-Vars in Subset are negated, all other Design_Vars are positive.
    Shield-Vars have same values then Design-Vars
    e.g. returns ~o1^~o1'^o2^o2'^~o3^~o3'^o4^o4',

    '''
    def createLabelFromSubset(self, subset):

        literals = []

        for designNr in self.specDfa_.getOutputVars():
            shieldNr = designNr+self.specDfa_.getVarNum()
            if designNr in subset:
                literals.append(designNr*-1)
                literals.append(shieldNr*-1)
            else:
                literals.append(designNr)
                literals.append(shieldNr)

        return DfaLabel(literals)

