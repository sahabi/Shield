from parser.dfaparser import DfaParser
from encoding.synthesizer import  Synthesizer

def make_shield(files = None): # IGNORE:C0111
    spec_files = files
    spec_dfas=[]

    for i in range(0, len(spec_files)):
        dfa_parser = DfaParser(spec_files[i])
        spec_dfas.append(dfa_parser.getParsedDFA())

    #use common input and output vairables
    spec_dfas = spec_dfas[0].buildAutomataWithCommonVariables(spec_dfas)

    #build product DFA
    prod_dfa = spec_dfas[0]
    for i in range(1, len(spec_dfas)):
        prod_dfa = prod_dfa.buildProductOfAutomata(spec_dfas[i])
        prod_dfa = prod_dfa.combineUnsafeStates()
        prod_dfa = prod_dfa.standardization(True)

    # build Violation,Correctness and Deviation Automaton
    shield_dfa = prod_dfa

    synthesis = Synthesizer(shield_dfa, interactive = False, instance = True)
    return synthesis
    
if __name__ == "__main__":
    files = ['/home/sahabi/shield/ShieldingHumans/inputfiles/uav/map_8_states/adversary.dfa']
    shield = make_shield(files)
    print shield.check('g', state = 200, inp = [], outp = None)
    print shield.check('b', state = 2, inp = [], outp = None)
    print shield.check('c', state = 4, inp = [2], outp = [0])