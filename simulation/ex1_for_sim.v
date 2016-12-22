/**************************************
* Simulation for inputfiles   
*   inputfiles/ex1.dfa
***************************************/

module main;
  // Input of DUT:
  reg clk;
  reg r;
  reg a1;
  reg a2;
  reg b1;
  reg b2;

  // Output of the DUT:
  wire a1__1;
  wire a2__1;
  wire b1__1;
  wire b2__1;

  //Instantiate the DUT:
  shield s(clk, r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);
  
  // make clock toggle:
  always #5 clk = ~clk;
  
  // Sequence of input stimuli to test with:
  initial begin
    clk = 0;

    r = 0;
    a1 = 0;
    a2 = 0;
    b1 = 0;
    b2 = 0;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

    //time=11 -------------------------------------------------
    #9
    r = 0;
    a1 = 1;
    a2 = 0;
    b1 = 0;
    b2 = 1;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

    $display("System Error. Shield has to deviate.");    
    //time=21 -------------------------------------------------
    #9
    r = 1;
    a1 = 1;
    a2 = 0;
    b1 = 1;
    b2 = 0;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

    //time=31 -------------------------------------------------
    #9
    r = 0;
    a1 = 1;
    a2 = 1;
    b1 = 1;
    b2 = 0;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

  
    //time=41 -------------------------------------------------
    #9
    r = 1;
    a1 = 0;
    a2 = 0;
    b1 = 1;
    b2 = 0;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

    $display("System Error. Shield has to deviate."); 

    //time=51 -------------------------------------------------
    #9
    r = 1;
    a1 = 0;
    a2 = 0;
    b1 = 0;
    b2 = 0;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);

   //time=61 -------------------------------------------------
    #9
    r = 0;
    a1 = 1;
    a2 = 1;
    b1 = 1;
    b2 = 1;
    #1
    $display("Time = %d, System Input: r=%d System Output: a1=%d a2=%d b1=%d b2=%d Shield Output a1=%d a2=%d b1=%d b2=%d", 
             $time, 
             r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);


    #1 $finish;         
  end
endmodule

module shield(clock, r, a1, a2, b1, b2, a1__1, a2__1, b1__1, b2__1);
  input clock;
  input r;
  input a1;
  input a2;
  input b1;
  input b2;
  output a1__1;
  output a2__1;
  output b1__1;
  output b2__1;

  wire s0n;
  wire s1n;
  wire tmp1;
  wire tmp2;
  wire tmp3;
  wire tmp4;
  wire tmp5;
  wire tmp6;
  wire tmp7;
  wire tmp8;
  wire tmp9;
  wire tmp10;
  wire tmp11;
  wire tmp12;
  wire tmp13;
  wire tmp14;
  wire tmp15;
  wire tmp16;
  wire tmp17;
  wire tmp18;
  wire tmp19;
  wire tmp20;

  reg s0;
  reg s1;

  assign tmp1 = a1 ? 1 : 0;
  assign a1__1 = tmp1;

  assign tmp3 = a2 ? 1 : 0;
  assign tmp4 = s0 ? 1 : tmp3;
  assign tmp2 = s1 ? tmp3 : tmp4;
  assign a2__1 = tmp2;

  assign tmp6 = b1 ? 1 : 0;
  assign tmp9 = a1 ? 1 : 0;
  assign tmp10 = ~(b1 ? 1 : 0);
  assign tmp8 = ~(r ? tmp9 : tmp10);
  assign tmp7 = s0 ? tmp6 : tmp8;
  assign tmp5 = s1 ? tmp6 : tmp7;
  assign b1__1 = tmp5;

  assign tmp12 = b2 ? 1 : 0;
  assign tmp11 = s1 ? 1 : tmp12;
  assign b2__1 = tmp11;

  assign tmp16 = a1 ? 1 : 0;
  assign tmp15 = r ? tmp16 : 1;
  assign tmp14 = s0 ? 1 : tmp15;
  assign tmp13 = ~(s1 ? 1 : tmp14);
  assign s1n = tmp13;

  assign tmp20 = a1 ? 1 : 0;
  assign tmp19 = ~(r ? tmp20 : 0);
  assign tmp18 = s0 ? 1 : tmp19;
  assign tmp17 = ~(s1 ? 1 : tmp18);
  assign s0n = tmp17;

  initial
   begin
    s0 = 0;
    s1 = 0;
   end

  always @(posedge clock)
   begin
    s0 = s0n;
    s1 = s1n;
   end
endmodule

