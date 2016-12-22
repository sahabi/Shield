'''
Created on Jun 10, 2014

@author: bkoenighofer
'''

 # -*- coding: utf-8 -*-

import pycudd
import math
from itertools import combinations

class PySynthesizer(object):
    '''
    Takes Violation, Correctness and Deviation Monitors.
    Synthesis Procedure computes the admissible strategy for the product of these automata,
    The final synthesis result can be given in Verilog.
    '''

    def __init__(self, shield_dfa, interactive, instance):
        #init pycudd
        self.mgr_ = pycudd.DdManager()
        self.mgr_.SetDefault()

        #init member vars
        self.shield_dfa_ = shield_dfa
        self.interactive_ = interactive
        self.instance_ = instance

        self.input_vars_ = []
        self.output_vars_ = []
        self.in_out_var_names_ = dict()
        self.num_of_bits_ = 0
        self.var_names_ = [] #list of all state bits, input and output variabes

        self.state_offsets_ = dict()
        self.var_bdds_ = dict()

        self.init_state_bdd_ = self.mgr_.One()
        self.transition_bdd_ = self.mgr_.One()
        self.err_state_bdd_ = self.mgr_.Zero()

        self.tmp_count_= 1
        self.result_model_ = ""

        self.synthesize()

    def synthesize(self):

        #add input vars
        for input_var in self.shield_dfa_.getInputVars():
            self.input_vars_.append(input_var)
            self.in_out_var_names_[input_var]= self.shield_dfa_.getVarName(input_var)

        #add output vars
        for output_var in self.shield_dfa_.getOutputVars():
            self.output_vars_.append(output_var)
            self.in_out_var_names_[output_var]= self.shield_dfa_.getVarName(output_var)

        #encode states and create init_state
        # (create state bdds for all state bits of all automata)
        state_order= self.encode_states_and_create_init_state()

        #encode variables
        var_order = self.encode_variables()

        #build next state vars
        self.next_state_vars_bdd_ = []
        for state_pos in range(0,self.num_of_bits_):
            self.next_state_vars_bdd_.append(self.var_bdds_['self.s'+str(self.num_of_bits_-1-state_pos)])

        #build input variables bdds
        self.in_var_bdds_ = []
        for var in self.input_vars_:
            self.in_var_bdds_.append(self.var_bdds_["v"+str(var-1)])

        #build output variables bdds
        self.out_var_bdd_ = []
        for var in self.output_vars_:
            self.out_var_bdd_.append(self.var_bdds_["v"+str(var-1)])

        #print "variable order to console"
        #print("variable order:"+state_order+var_order)

        #encode transition relation for each dfa
        self.transition_bdd_ = self.encode_transitions(self.shield_dfa_)

        #print "Final Transition_BDD:"
        #self.transition_bdd_.PrintMinterm()

        #create error states
        # - states where shield violates the spec or makes an invalid deviation
        self.create_error_states()

        #calculate safety winning region
        self.win_region_ = self.calc_safety_winning_region()
        #print("safety winning region:")
        #self.safety_win_region_.PrintMinterm()

        self.func_by_var_ = dict()

        self.strategy = self.get_nondet_strategy_safety_game()

        if self.interactive_:
            self.interactive()

        if self.instance_:
            self.instance()

        #comute next states functions bdd and output functions bdd
        if not self.instance_:
            self.func_by_var_ = self.extract_output_funcs()


    def getResultModel(self):

        if self.func_by_var_ == dict():
            print "Synthesis was not successful"
        if self.win_region_ == self.mgr_.Zero():
            print "Winning region is empty"

        #encode output function bdd in verilog
        for var_num in self.output_vars_:
            var_bdd = self.var_bdds_["v"+str(var_num-1)]
            var_lit = var_bdd.NodeReadIndex()
            var_name = self.var_names_[var_lit]
            self.model_to_output_format(var_name, var_bdd, self.func_by_var_[var_bdd])

        #encode next state function bdd in verilog
        for state_pos in range(0,self.num_of_bits_):
            state_name = 'self.s'+str(self.num_of_bits_-1-state_pos)
            state_bdd = self.var_bdds_[state_name]
            self.model_to_output_format(state_name, state_bdd, self.func_by_var_[state_bdd])

        self.result_model_ += '        return ('

        for var_num in self.output_vars_:
            var_bdd = self.var_bdds_["v"+str(var_num-1)]
            var_lit = var_bdd.NodeReadIndex()
            var_name = self.var_names_[var_lit]
            self.result_model_ += var_name + ', '
        self.result_model_=self.result_model_[0:len(self.result_model_)-2]
        self.result_model_ += ')'

        return self.result_model_

    def getNumOfBits(self):
        return self.num_of_bits_

    def getTmpCount(self):
        return self.tmp_count_

    def existsWinningRegion(self):
        if self.win_region_ != self.mgr_.Zero():
            return True
        else:
            return False

    def encode_states_and_create_init_state(self):

        self.num_of_bits_ = int(math.ceil(math.log(len(self.shield_dfa_.getNodes()), 2)))

        state_order=""

        #create var bdds
        for state_pos in range(0, self.num_of_bits_):
            node_bdd = self.mgr_.IthVar(len(self.var_bdds_))
            state_name = 's'+str(self.num_of_bits_-1-state_pos)
            self.var_names_.append(state_name)
            self.var_bdds_[state_name]=node_bdd
            state_order += state_name + " "

        for state_pos in range(0, self.num_of_bits_):
            node_bdd = self.mgr_.IthVar(len(self.var_bdds_))
            state_name = 'self.s'+str(self.num_of_bits_-1-state_pos)
            self.var_names_.append(state_name)
            self.var_bdds_[state_name]=node_bdd
            state_order += state_name + " "

        #create initial state bdd
        init_state_et = self.shield_dfa_.getInitialNodes()[0]
        self.init_state_bdd_ &= self.make_node_state_bdd(init_state_et.getNr()-1)

        #print "Init_state_BDD"
        #self.init_state_bdd_.PrintMinterm()
        return state_order

    def encode_variables(self):
        var_order=""
        for var in self.in_out_var_names_:
            var_num = var-1
            var_name = self.in_out_var_names_[var]
            var_order += var_name+" "
            self.var_names_.append(var_name)
            node_bdd = self.mgr_.IthVar(len(self.var_bdds_))
            self.var_bdds_["v"+str(var_num)] = node_bdd
            self.var_bdds_["v"+str(var_num)] = node_bdd
        return var_order

    def encode_transitions(self, dfa):

        transition_bdd = self.mgr_.Zero()

        edges = dfa.getEdges()
        for edge in edges:
            source = edge.getSourceNode().getNr()
            target = edge.getTargetNode().getNr()
            literals = edge.getLabel().getLiterals()

            #encode state and next_state for this edge
            source_state_bdd = self.make_node_state_bdd(source-1)
            target_state_bdd = self.make_node_state_next_bdd(target-1)
            edge_transition = source_state_bdd
            edge_transition &= target_state_bdd

            #encode literals for this edge
            for literal in literals:
                sign = literal > 0
                abs_literal = abs(literal)
                assert(abs_literal!=0)
                var_literal=self.var_bdds_["v"+str(abs_literal-1)]
                if sign:
                    edge_transition &= var_literal
                else:
                    edge_transition &= ~var_literal

            transition_bdd += edge_transition

        #print "Transition_BDD"
        #transition_bdd.PrintMinterm()
        return transition_bdd


    def create_error_states(self):

        self.err_state_bdd_ = self.mgr_.Zero()

        #All unsafe states are error states
        for state in self.shield_dfa_.getNodes():
            if state.isFinal():
                self.err_state_bdd_ += self.make_node_state_bdd(state.getNr()-1)

        #print "Error_BDD:"
        #self.err_state_bdd_.PrintMinterm()

    def calc_safety_winning_region(self):

        not_error_bdd = ~self.err_state_bdd_
        new_set_bdd = self.mgr_.One()
        while True:
            curr_set_bdd = new_set_bdd
            new_set_bdd = not_error_bdd & self.pre_sys_bdd(curr_set_bdd, self.transition_bdd_)

            if (new_set_bdd & self.init_state_bdd_) == self.mgr_.Zero():
                return self.mgr_.Zero()

            if new_set_bdd == curr_set_bdd:
                return new_set_bdd

    def suc_sys_bdd(self, src_states_bdd, transition_bdd):
        abstract_bdd = self.get_cube(self.out_var_bdd_ + self.in_var_bdds_ + self.get_all_state_bdds())

        suc_bdd = transition_bdd.AndAbstract(src_states_bdd, abstract_bdd)

        return self.prime_states(suc_bdd)


    def pre_bdd(self, dst_states_bdd, transition_bdd, cooperative):
        if cooperative:
            return self.pre_cooperative_bdd(dst_states_bdd, transition_bdd)
        else:
            return self.pre_sys_bdd(dst_states_bdd, transition_bdd)


    def pre_sys_bdd(self, dst_states_bdd, transition_bdd):
        """ Calculate predecessor states of given states.

        :return: BDD representation of predecessor states

        :hints: if current states are not primed they should be primed before calculation (why?)
        :hints: calculation of ``o t(a,b,o)`` using cudd: ``t.ExistAbstract(get_cube(o))``
        :hints: calculation of ``i t(a,b,i)`` using cudd: ``t.UnivAbstract(get_cube(i))``
        """

        #: :type: DdNode
        transition_bdd = transition_bdd
        #: :type: DdNode
        primed_dst_states_bdd = self.prime_states(dst_states_bdd)

        #: :type: DdNode
        intersection = transition_bdd & primed_dst_states_bdd  # all predecessors (i.e., if sys and env cooperate)

        # cudd requires to create a cube first..
        if len(self.out_var_bdd_) != 0:
            out_vars_cube_bdd = self.get_cube(self.out_var_bdd_)
            exist_outs = intersection.ExistAbstract(out_vars_cube_bdd)
        else:
            exist_outs = intersection
        # print
        # print
        #
        # print('exist_outs: quantified vars')
        # print"0123456789"
        # out_vars_cube_bdd.PrintMinterm()
        # print('before quantifying')
        # intersection.PrintMinterm()
        # print('after quantifying')
        # exist_outs.PrintMinterm()

        next_state_vars_cube = self.prime_states(self.get_cube(self.get_all_state_bdds()))
        exist_next_state = exist_outs.ExistAbstract(next_state_vars_cube)

        # print('exists_next_states: quantified vars')
        # next_state_vars_cube.PrintMinterm()
        # print('before quantifying')
        # exist_outs.PrintMinterm()
        # print('after quantifying')
        # exist_next_state.PrintMinterm()

        uncontrollable_output_bdds = self.in_var_bdds_
        if len(self.in_var_bdds_) !=0:
            in_vars_cube_bdd = self.get_cube(uncontrollable_output_bdds)
            forall_inputs = exist_next_state.UnivAbstract(in_vars_cube_bdd)
        else:
            forall_inputs = exist_next_state

        # print('forall_exists')
        # forall_inputs.PrintMinterm()

        return forall_inputs

    def checkInteractiveInput(self, command, state_nr, in_literals, output_literals):

        if False:
            print
            print "    DEBUG: performing the following check:"
            print "            - type:  " + command
            print "            - state: " + str(state_nr)
            print "            - input: " + str(in_literals).translate(None, "'")
            if command == 'c':
                print "            - output to check: " + str(output_literals).translate(None, "'")
            print

        state_bdd = self.make_node_state_bdd(state_nr-1)

        in_var_bdd = self.mgr_.One()
        for literal in in_literals:
            sign = literal > 0
            var_literal=self.var_bdds_["v"+str(abs(literal)-1)]
            if sign:
                in_var_bdd &= var_literal
            else:
                in_var_bdd &= ~var_literal

        allowed_output_bdd = state_bdd & in_var_bdd & self.strategy

        if command=='c':
            out_var_bdd = self.mgr_.One()
            for literal in in_literals:
                sign = literal > 0
                var_literal=self.var_bdds_["v"+str(abs(literal)-1)]
                if sign:
                    out_var_bdd &= var_literal
                else:
                    out_var_bdd &= ~var_literal

            if (out_var_bdd & allowed_output_bdd) != self.mgr_.Zero():
                return "allowed"
            else:
                return "disallowed"


        #compute all don't-care-outputs
        # => outputs that don't change anything in this situation
        # add only output that make a difference in the final output set

        vip_output_vars = []
        all_outputs = list(self.out_var_bdd_)
        arena = allowed_output_bdd.ExistAbstract(self.get_cube(self.get_all_state_bdds()+ self.in_var_bdds_))

        for var in self.output_vars_:
            c = self.var_bdds_["v"+str(var-1)]

            if arena.ExistAbstract(c) != arena: #can_be_true == self.mgr_.One() and can_be_false == self.mgr_.One():
                vip_output_vars.append(var)


        #create list of all possible outputs
        possible_out_literals = []
        pos_outputs = sum([map(list, combinations(vip_output_vars, i)) for i in range(len(vip_output_vars) + 1)], [])
        for pos_output in pos_outputs:
            neg_output = list(set(vip_output_vars)-set(pos_output))
            neg_output = [x*-1 for x in neg_output]
            possible_out_literals.append(list(set().union(pos_output,neg_output)))


        if command=='g':
            #return list of all good outputs
            allowedList=[]

            for out_literals in possible_out_literals:
                out_var_bdd = self.mgr_.One()
                for literal in out_literals:
                    sign = literal > 0
                    var_literal=self.var_bdds_["v"+str(abs(literal)-1)]
                    if sign:
                        out_var_bdd &= var_literal
                    else:
                        out_var_bdd &= ~var_literal

                if (out_var_bdd & allowed_output_bdd) != self.mgr_.Zero():
                    allowedList.append(out_literals)
                    #print "Yes: the output " + str(out_literals).translate(None, "'") +" is allowed"

            return allowedList

        if command=='b':
            #return list of all good outputs
            disallowedList=[]

            for out_literals in possible_out_literals:
                out_var_bdd = self.mgr_.One()
                for literal in out_literals:
                    sign = literal > 0
                    var_literal=self.var_bdds_["v"+str(abs(literal)-1)]
                    if sign:
                        out_var_bdd &= var_literal
                    else:
                        out_var_bdd &= ~var_literal

                if (out_var_bdd & allowed_output_bdd) == self.mgr_.Zero():
                    disallowedList.append(out_literals)
                #print "No: the output " + str(out_literals).translate(None, "'") +" is not allowed"
            return disallowedList

        print "na"

    def instance(self):
        pass

    def check(self, cmd, state, inp = None, outp = None):
        # self.checkInteractiveInput(command,state, in_literals, out_literals)
        try:
            if outp:
                literals = inp + ['o'] + outp
            else:
                literals = inp
            out_literals=[]

            #for check command, test for output definition
            idx=0
            try:
                idx = literals.index('o')
                output=literals[idx+1:]
                literals=literals[:idx]

                if len(output)<1:
                    print "you need to specify at least one output literal"
                    return False

                try:
                    for o in output:
                        out_literals.append(int(o))
                except ValueError:
                    print "all output literals have to be an int"
                    return False

            except ValueError:
                if cmd[0]=='c':
                    print "this command type requires an output"
                    return False

            in_literals=[]
            for l in literals:
                in_literals.append(int(l))

            if cmd[0]=='c' and len(out_literals)==0:
                print "you need at least one output literal using this command type"
                return False
            return self.checkInteractiveInput(cmd[0],state, in_literals, out_literals)
        except ValueError:
            print 'all literals have to be an int'

    def interactive(self):
        """ Call shield in interactive Mode

        Possible Commands:

        command> g state_nr [input_literals]
        returns all Good outputs possible for a certain state and input,
        if literals are not contained at all, they don't matter and can be pos or negative

        command> b state_nr [input_literals]
        returns all Bad outputs for a certain state and input
        if literals are not contained at all, they don't matter and can be pos or negative

        command> c state_nr [input_literals] o [output_literals]
        Checks if an output is allowed for a certain state and input

        command> q
        quit
        """

        while(True):
            cmd = str(raw_input("command>")).strip()
            if cmd == "q":
                break
            else:
                if len(cmd)<1:
                    print "unknown command"
                else:
                    if (cmd[0]=='g' or cmd[0]=='b' or cmd[0]=='c') and len(cmd)>=5:
                        if cmd[1]==' ':
                            params = cmd[2:].split()
                            if len(params)< 1:
                                print "command parameters missing"
                            else:
                                state=params[0]
                                try:

                                    state=int(state)

                                    try:
                                        literals=params[1:]
                                        out_literals=[]

                                        #for check command, test for output definition
                                        idx=0
                                        try:
                                            idx = literals.index('o')
                                            output=literals[idx+1:]
                                            literals=literals[:idx]

                                            if len(output)<1:
                                                print "you need to specify at least one output literal"
                                                continue

                                            try:
                                                for o in output:
                                                    out_literals.append(int(o))
                                            except ValueError:
                                                print "all output literals have to be an int"
                                                continue

                                        except ValueError:
                                            if cmd[0]=='c':
                                                print "this command type requires an output"
                                                continue

                                        in_literals=[]
                                        for l in literals:
                                            in_literals.append(int(l))

                                        if cmd[0]=='c' and len(out_literals)==0:
                                            print "you need at least one output literal using this command type"
                                            continue
                                        self.checkInteractiveInput(cmd[0],state, in_literals, out_literals)

                                    except ValueError:
                                        print 'all literals have to be an int'

                                except ValueError:
                                    print 'state has to be an int'
                        else:
                            print "syntax error"
                    else:
                        print "syntax error"

    def get_nondet_strategy_safety_game(self):
        """ Get non-deterministic strategy from the winning region.
        If the system outputs values that satisfy this non-deterministic strategy, then the system wins.
        I.e., a non-deterministic strategy describes for each state all possible plausible output values:

        :return: non deterministic strategy bdd
        :note: The strategy is still not-deterministic. Determinization step is done later.
        """

        #: :type: DdNode
        primed_win_region_bdd = self.prime_states(self.win_region_)

        #print "primed_win_region_bdd"
        #primed_win_region_bdd.PrintMinterm()

        intersection = (primed_win_region_bdd & self.transition_bdd_) # all predecessors (i.e., if sys and env cooperate)

        #print "intersection"
        #intersection.PrintMinterm()

        next_vars_cube = self.prime_states(self.get_cube(self.get_all_state_bdds()))
        strategy = intersection.ExistAbstract(next_vars_cube)

        #print "nondet strategy"
        #print strategy.PrintMinterm()

        return strategy


    def extract_output_funcs(self):
        """
        Calculate BDDs for output functions given a non-deterministic winning strategy.
        Cofactor-based approach.

        :return: dictionary ``controllable_variable_bdd -> func_bdd``
        """

        output_models = dict()
        all_outputs = list(self.out_var_bdd_)
        all_next_state_vars = list(self.next_state_vars_bdd_)
        all_next_states_and_outputs = all_outputs + all_next_state_vars



        #----------- output functions--------------

        for c in self.out_var_bdd_:

            others = set(set(all_outputs).difference({c}))

            if others:
                others_cube = self.get_cube(others)
                #: :type: DdNode
                c_arena = self.strategy.ExistAbstract(others_cube)
            else:
                c_arena = self.strategy

            can_be_true = c_arena.Cofactor(c)  # states (x,i) in which c can be true
            can_be_false = c_arena.Cofactor(~c)

            #print'can_be_true'
            #can_be_true.PrintMinterm()
            #print'can_be_false'
            #can_be_false.PrintMinterm()
            #print

            # We need to intersect with can_be_true to narrow the search.
            # Negation can cause including states from !W (with err=1)
            #: :type: DdNode
            must_be_true = (~can_be_false) & can_be_true
            must_be_false = (~can_be_true) & can_be_false

            #print "must_be_true"
            #must_be_true.PrintMinterm()
            #print "must_be_false"
            #must_be_false.PrintMinterm()
            #print

            care_set = (must_be_true | must_be_false)
            
            # begin compute reachable states:
            # reach = self.init_state_bdd_
            # old_reach = self.mgr_.Zero()
            # while reach != old_reach:
            #     old_reach = reach
            #     reach = reach | self.suc_sys_bdd(reach, non_det_strategy & self.transition_bdd_ )
            # care_set = care_set & reach
            # end compute reachable states

            #print'care set is'
            #care_set.PrintMinterm()

            # We use 'restrict' operation, but we could also do just:
            # c_model = must_be_true -> care_set
            # ..but this is (probably) less efficient, since we cannot set c=1 if it is not in care_set, but we could.
            #
            # Restrict on the other side applies optimizations to find smaller bdd.
            # It cannot be expressed using boolean logic operations since we would need to say:
            # must_be_true = ite(care_set, must_be_true, "don't care")
            # and "don't care" cannot be expressed in boolean logic.

            # Restrict operation:
            #   on care_set: must_be_true.restrict(care_set) <-> must_be_true
            c_model = must_be_true.Restrict(care_set)

            output_models[c] = c_model

            self.strategy = self.strategy & self.make_bdd_eq(c, c_model)

            #print "Strategy for output variable "
            #c.PrintMinterm()

            #print'on_set: Var is True'
            #c_model.PrintMinterm()
            #print'off_set: Var is False'
            #(~c_model).PrintMinterm()

        #----------- next state functions--------------

        self.strategy = self.strategy & self.transition_bdd_

        for c in self.next_state_vars_bdd_:
            others = set(set(all_next_states_and_outputs).difference({c}))
            if others:
                others_cube = self.get_cube(others)
                #: :type: DdNode
                c_arena = self.strategy.ExistAbstract(others_cube)
            else:
                c_arena = self.strategy

            can_be_true = c_arena.Cofactor(c)  # states (x,i) in which c can be true
            can_be_false = c_arena.Cofactor(~c)

            must_be_true = (~can_be_false) & can_be_true
            must_be_false = (~can_be_true) & can_be_false

            care_set = (must_be_true | must_be_false)

            c_model = must_be_true.Restrict(care_set)

            output_models[c] = c_model

            self.strategy = self.strategy & self.make_bdd_eq(c, c_model)

        return output_models


    def get_cube(self,variables):
        assert len(variables)

        cube = self.mgr_.One()
        for v in variables:
            cube &= v
        return cube


    def make_bdd_eq(self,value1, value2):
        return (value1 & value2) | (~value1 & ~value2)


    def get_all_state_bdds(self):
        states=[]
        for i in range(0,self.num_of_bits_):
            states.append(self.var_bdds_["s"+str(i)])
        return states

    def prime_states(self,unprimed_states):
        all_var_bdds=self.var_bdds_.values()
        num_bdds= len(all_var_bdds)

        #: :type: DdArray
        primed_var_array = pycudd.DdArray(num_bdds)
        curr_var_array = pycudd.DdArray(num_bdds)

        for l_bdd in all_var_bdds:
            #: :type: DdNode
            l_bdd = l_bdd
            curr_var_array.Push(l_bdd)
            lit = l_bdd.NodeReadIndex()

            #range of current state bits, is moved by len of state field
            if 0 <= lit < self.num_of_bits_:
                new_l_bdd = self.mgr_.IthVar(lit+self.num_of_bits_)
            else:
                new_l_bdd = l_bdd

            primed_var_array.Push(new_l_bdd)

        replaced_states_bdd = unprimed_states.SwapVariables(curr_var_array, primed_var_array, num_bdds)

        return replaced_states_bdd

    def make_node_state_bdd(self, nodeNr):

        bin_node_nr = bin(int(nodeNr))[2:]
        bin_str = ""+bin_node_nr.zfill(self.num_of_bits_)

        result = self.mgr_.One()
        j = 1
        for i in range(0,self.num_of_bits_):
            sign = bin_str[len(bin_str)-j] #sign of s
            if int(sign)==1:
                result &= self.var_bdds_["s"+str(i)] #bdd of s
            elif int(sign)==0:
                result &= ~self.var_bdds_["s"+str(i)]
            j=j+1

        return result

    def make_node_state_next_bdd(self,nodeNr):

        bin_node_nr = bin(int(nodeNr))[2:]
        bin_str = ""+bin_node_nr.zfill(self.num_of_bits_)

        result = self.mgr_.One()
        j = 1
        for i in range(0,self.num_of_bits_):
            sign = bin_str[len(bin_str)-j] #sign of s
            if int(sign)==1:
                result &= self.var_bdds_["self.s"+str(i)] #bdd of s
            elif int(sign)==0:
                result &= ~self.var_bdds_["self.s"+str(i)]
            j=j+1
        return result

    def walk(self, a_bdd):
        """
        Walk given BDD node (recursively).

        :returns: literal representing input BDD
        :warning: variables in cudd nodes may be complemented, check with: ``node.IsComplement()``
        """

        #: :type: DdNode
        a_bdd = a_bdd
        if a_bdd.IsConstant():
            if a_bdd == self.mgr_.One():
                return "True"
            else:
                return "False"

        #check if bdd node was already visited
        if a_bdd in self.visited_:
            return self.visited_[a_bdd]

        node_name = "tmp" + str(self.tmp_count_)
        self.tmp_count_ = self.tmp_count_ + 1

        self.visited_[a_bdd] = node_name
        self.bdd_node_counter_ = self.bdd_node_counter_ + 1

        # get an index of variable,
        a_lit = a_bdd.NodeReadIndex()

        #: :type: DdNode
        t_bdd = a_bdd.T()
        #: :type: DdNode
        e_bdd = a_bdd.E()

        t_lit = self.walk(t_bdd)
        e_lit = self.walk(e_bdd)

        a_name = self.var_names_[a_lit]
        if a_name[0] == 's':
            ite_lit = 'evaluate(self.{0}, {1}, {2})'.format(a_name, t_lit, e_lit)
        else:
            ite_lit = 'evaluate({0}, {1}, {2})'.format(a_name, t_lit, e_lit)
        if a_bdd.IsComplement():
            self.output_model_ += "        " + node_name + " = " + 'inv_'+ ite_lit + ";\n"
        else:
            self.output_model_ += "        " + node_name + " = " + ite_lit + ";\n"

        return node_name

    def model_to_output_format(self, c_name, c_bdd, func_bdd):
        """ encodes definition of output variable c
        """
        #: :type: DdNode

        c_bdd = c_bdd

        self.visited_ = dict()
        self.bdd_node_counter_ = 1
        self.output_model_ = ""

        top_level_var = self.walk(func_bdd)
        self.output_model_ += '        ' + c_name + " = " + top_level_var  + ";\n"
        self.result_model_ += self.output_model_ + "\n"










