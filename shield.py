#!/usr/local/bin/python2.7
# encoding: utf-8
'''
shield -- shielded synthesis tool

shield is the first shield synthesize tool.

It defines classes_and_methods

@author:     Bettina Könighofer, Robert Könighofer

@copyright:  2014 IAIK, Graz University of Technology. All rights reserved.

@license:    license

@contact:    bettina.koennighofer@iaik.tugraz.at, robert.koenighofer@iaik.tugraz.at
'''

import sys
import os
import time

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

from parser.dfaparser import DfaParser
from algorithm.dfaGenerator import DfaGenerator
from encoding.pysynthesizer import  PySynthesizer
from encoding.pythonencoder import PyEncoder
from encoding.synthesizer import  Synthesizer
from encoding.verilogencoder import VerilogEncoder


__all__ = []
__version__ = 0.1
__date__ = '2014-06-03'
__updated__ = '2014-06-04'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created on %s.
  Copyright 2014 IAIK, Graz University of Technology. All rights reserved.

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    t_total = time.time()

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument('--interactive',action="store_true", help="Use Shield in the interactive Mode")
        parser.add_argument('--py',action="store_true", help="generate python shield")
        parser.add_argument('spec_file', nargs='+')

        # Process arguments
        args = parser.parse_args()
        spec_files = args.spec_file

        #output file name is a combination of all input file names
        output_file_name="output/"
        for input_file in spec_files:
            input_file_name = input_file.split("/")
            input_file_name = input_file_name[len(input_file_name)-1]
            input_file_name = input_file_name.split(".")[0]
            output_file_name+=input_file_name+"_"
        output_file_name = output_file_name[:-1]

        interactive = False
        python = False
        if args.interactive:
            interactive = True
        if args.py:
            python = True
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


    #print initial message
    print("************************************************")
    print("* Setup for Shield Synthesis:")
    print("** Synthesize Shields for Human Operators")

    if interactive:
        print "** Use Shield in interactive Mode"

    print("** Output File in Verilog Format")
    print("** Used specification automaton input files:")
    for spec_file in spec_files:
        print("*** "+ spec_file)
    print("************************************************\n")

    spec_dfas=[]
    for i in range(0, len(args.spec_file)):
        dfa_parser = DfaParser(args.spec_file[i])
        spec_dfas.append(dfa_parser.getParsedDFA())

    #use common input and output vairables
    spec_dfas = spec_dfas[0].buildAutomataWithCommonVariables(spec_dfas)

    #print("Specification DFA")
    #for spec_dfa in spec_dfas:
    #   spec_dfa.debugPrintDfa()

    #build product DFA
    prod_dfa = spec_dfas[0]
    for i in range(1, len(spec_dfas)):
        prod_dfa = prod_dfa.buildProductOfAutomata(spec_dfas[i])
        prod_dfa = prod_dfa.combineUnsafeStates()
        prod_dfa = prod_dfa.standardization(True)

    # build Violation,Correctness and Deviation Automaton
    dfa_generator = DfaGenerator(prod_dfa)
    if interactive:
        shield_dfa = prod_dfa
    else:
        shield_dfa = dfa_generator.buildShieldAutomaton()
    if python:
        synthesis = PySynthesizer(shield_dfa, interactive)

        #create output file
        python_encoder = PyEncoder(prod_dfa)
        python_encoder.addShieldModel(synthesis.getResultModel(), synthesis.getNumOfBits(), synthesis.getTmpCount())
        python_str = python_encoder.getEncodedData()
        with open(output_file_name+".py", "w+") as text_file:
            text_file.write(python_str)
    else:
        synthesis = Synthesizer(shield_dfa, interactive)
        #create output file
        encoder = VerilogEncoder(prod_dfa)
        encoder.addShieldModel(synthesis.getResultModel(), synthesis.getNumOfBits(), synthesis.getTmpCount())
        verilog_str = encoder.getEncodedData()
        with open(output_file_name+".v", "w+") as text_file:
                text_file.write(verilog_str)



    #print final message
    total_time = round(time.time() - t_total,2)

    print("******************************************")
    print("*** Total execution time: " + str(total_time) + "        ***")
    print("******************************************")

    return 100
    
    
if __name__ == "__main__":
    sys.exit(main())