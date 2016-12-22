This archive is meant for reviewers of FMCAD'16 to reproduce the 
experiments of the paper 'Shield Synthesis: Runtime Enforcement for 
Reactive Systems'. Upon acceptance, the source code and examples will be 
made publicly available (after cleaning up the code a bit, and maybe 
improving the performance some more).

Installing the tool:
====================
So far, this tool has been tested on Linux systems only. In order to 
make it run, you need to:
 - Make sure you have Python installed
 - Download and install PyCUDD [1] 
 - Add the directory in which you installed PyCUDD to your 
   LD_LIBRARY_PATH and PYTHONPATH environment variables. On Bash-like
   shells you can do this by typing
   export PYTHONPATH=$PYTHONPATH:/path_to/pycudd2.0.2/pycudd
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path_to/pycudd2.0.2/cudd-2.4.2/lib
   In order to avoid setting these variables each time, you can also add these
   two lines to the file ~/.bashrc.
 
Running our synthesis tool:
===========================
 - Open a shell in the directory where you extracted this archive. 
 - Execute
    > python ./shield.py -h
   to get a list of command-line arguments.
 - If you want a shield from a safety specification, then
   executing
    > python ./shield.py path/to/spec_automaton.dfa
   should be enough. You can also list several .dfa-files, then the tool
   automatically computes the product automaton. 
 - The safety specification automaton is defined with a very simple textual
   format. This format is described in the file docs/InputFormat.txt.
 - Example input files can be found in the directory 
   inputfiles/*

Reproducing the results from the paper:
=======================================

Motivation Example, Figure 3:
(UAV enters ROZ and stays for too long inside.)
-------------------------
- Execute
   > python ./shield.py inputfiles/uav/map_16_states/map.dfa inputfiles/uav/map_16_states/roz.dfa
  to synthesize a shield for this example in Verilog format. The result will be
  written to the file output/map_roz.v			
- To simulate the behavior of the shield, execute either:
   > veriwell ./simulation/map_16_states_for_sim.v
  or
   > iverilog ./simulation/map_16_states_for_sim.v
   > ./a.out
  depending on your favourite verilog simulator.
  You should get output like this:
	Time =                    1, loc_design=0000, loc_shield=0000
	Go to location 12: 1 -> 6 -> 3 -> 11 -> 12 -> 12 
	Time =                   11, loc_design=0101, loc_shield=0101
	Time =                   21, loc_design=0010, loc_shield=0010
	Time =                   31, loc_design=1010, loc_shield=1010
	Time =                   41, loc_design=1011, loc_shield=1011
	Time =                   51, loc_design=1011, loc_shield=1110 (Error by Design, ROZ)
	Time =                   61, loc_design=1100, loc_shield=1110
	Time =                   71, loc_design=1101, loc_shield=1101
  This is the simulation trace you can find in the paper.

Running the Tool in Interactive Mode:
=======================================
 - If you want the tool to be executed in interactive mode execute
    > python ./shield.py path/to/spec_automaton.dfa --interactive

 -  There are 4 different commands available:

     	command> g state_nr [input_literals]
        returns all GOOD outputs possible for a certain state and input,
        if literals are not contained at all, they don't matter and can be pos or negative

        command> b state_nr [input_literals]
        returns all BAD outputs for a certain state and input
        if literals are not contained at all, they don't matter and can be pos or negative

        command> c state_nr [input_literals] o [output_literals]
        CHECKS if an output is allowed for a certain state and input

        command> q
        quit
  
Have fun!

[1] http://bears.ece.ucsb.edu/pycudd.html
