module shield(clock, u1, l1, l2, l3, l1__1, l2__1, l3__1);
  input clock;
  input u1;
  input l1;
  input l2;
  input l3;
  output l1__1;
  output l2__1;
  output l3__1;

  wire s0n;
  wire s1n;
  wire s2n;
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
  wire tmp21;
  wire tmp22;
  wire tmp23;
  wire tmp24;
  wire tmp25;
  wire tmp26;
  wire tmp27;
  wire tmp28;
  wire tmp29;
  wire tmp30;
  wire tmp31;
  wire tmp32;
  wire tmp33;
  wire tmp34;
  wire tmp35;
  wire tmp36;
  wire tmp37;
  wire tmp38;
  wire tmp39;
  wire tmp40;
  wire tmp41;
  wire tmp42;
  wire tmp43;
  wire tmp44;
  wire tmp45;
  wire tmp46;
  wire tmp47;
  wire tmp48;
  wire tmp49;
  wire tmp50;

  reg s0;
  reg s1;
  reg s2;

  assign tmp3 = ~(l1 ? 1 : 0);
  assign tmp2 = s1 ? 1 : tmp3;
  assign tmp1 = ~(s2 ? tmp2 : tmp3);
  assign l1__1 = tmp1;

  assign tmp8 = l2 ? 1 : 0;
  assign tmp7 = l1 ? tmp8 : 0;
  assign tmp6 = ~(s0 ? tmp7 : tmp8);
  assign tmp5 = s1 ? 1 : tmp6;
  assign tmp9 = ~(l2 ? 1 : 0);
  assign tmp4 = ~(s2 ? tmp5 : tmp9);
  assign l2__1 = tmp4;

  assign tmp15 = ~(l3 ? 1 : 0);
  assign tmp14 = l2 ? 1 : tmp15;
  assign tmp13 = l1 ? tmp14 : 1;
  assign tmp17 = l3 ? 1 : 0;
  assign tmp18 = ~(l2 ? 1 : tmp15);
  assign tmp16 = ~(l1 ? tmp17 : tmp18);
  assign tmp12 = s0 ? tmp13 : tmp16;
  assign tmp11 = s1 ? 1 : tmp12;
  assign tmp10 = ~(s2 ? tmp11 : tmp15);
  assign l3__1 = tmp10;

  assign tmp22 = l1 ? 1 : 0;
  assign tmp25 = l3 ? 1 : 0;
  assign tmp24 = l2 ? 1 : tmp25;
  assign tmp23 = l1 ? 1 : tmp24;
  assign tmp21 = ~(s0 ? tmp22 : tmp23);
  assign tmp20 = s1 ? 1 : tmp21;
  assign tmp27 = s0 ? tmp23 : 0;
  assign tmp26 = ~(s1 ? tmp27 : 0);
  assign tmp19 = ~(s2 ? tmp20 : tmp26);
  assign s2n = tmp19;

  assign tmp31 = l1 ? 1 : 0;
  assign tmp30 = ~(s0 ? tmp31 : 0);
  assign tmp29 = s1 ? 1 : tmp30;
  assign tmp36 = l3 ? 1 : 0;
  assign tmp35 = l2 ? 1 : tmp36;
  assign tmp34 = ~(l1 ? 1 : tmp35);
  assign tmp33 = s0 ? 1 : tmp34;
  assign tmp38 = l1 ? 1 : tmp35;
  assign tmp37 = ~(s0 ? tmp38 : 0);
  assign tmp32 = s1 ? tmp33 : tmp37;
  assign tmp28 = ~(s2 ? tmp29 : tmp32);
  assign s1n = tmp28;

  assign tmp42 = l1 ? 1 : 0;
  assign tmp45 = l3 ? 1 : 0;
  assign tmp44 = l2 ? 1 : tmp45;
  assign tmp43 = l1 ? 1 : tmp44;
  assign tmp41 = ~(s0 ? tmp42 : tmp43);
  assign tmp40 = s1 ? 1 : tmp41;
  assign tmp48 = ~(l1 ? 1 : tmp44);
  assign tmp47 = s0 ? 1 : tmp48;
  assign tmp50 = ~(u1 ? tmp43 : 0);
  assign tmp49 = s0 ? 1 : tmp50;
  assign tmp46 = s1 ? tmp47 : tmp49;
  assign tmp39 = ~(s2 ? tmp40 : tmp46);
  assign s0n = tmp39;

  initial
   begin
    s0 = 0;
    s1 = 0;
    s2 = 0;
   end

  always @(posedge clock)
   begin
    s0 = s0n;
    s1 = s1n;
    s2 = s2n;
   end
endmodule

