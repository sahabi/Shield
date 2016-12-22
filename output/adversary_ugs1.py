def evaluate(operand, a, b):
    if operand:
        return a
    else:
        return b

def inv_evaluate(operand, a, b):
    if operand:
        return not a
    else:
        return not b 


class Shield(object):
    def __init__(self):
        self.s0 = False;
        self.s1 = False;
        self.s2 = False;
        self.s3 = False;
        self.s4 = False;
    def move(self,u1, l1, l2, l3):
        tmp4 = inv_evaluate(l1, True, False);
        tmp3 = evaluate(self.s1, True, tmp4);
        tmp2 = evaluate(self.s2, True, tmp3);
        tmp1 = inv_evaluate(self.s4, tmp2, tmp4);
        l1__1 = tmp1;

        tmp11 = evaluate(l2, True, False);
        tmp10 = evaluate(l1, tmp11, False);
        tmp9 = evaluate(self.s0, tmp10, False);
        tmp13 = inv_evaluate(l2, True, False);
        tmp12 = inv_evaluate(self.s0, True, tmp13);
        tmp8 = evaluate(self.s1, tmp9, tmp12);
        tmp15 = inv_evaluate(self.s0, tmp11, False);
        tmp14 = inv_evaluate(self.s1, True, tmp15);
        tmp7 = evaluate(self.s2, tmp8, tmp14);
        tmp18 = evaluate(self.s0, True, tmp13);
        tmp17 = evaluate(self.s1, tmp18, True);
        tmp19 = evaluate(self.s1, True, tmp13);
        tmp16 = inv_evaluate(self.s2, tmp17, tmp19);
        tmp6 = inv_evaluate(self.s3, tmp7, tmp16);
        tmp5 = inv_evaluate(self.s4, True, tmp6);
        l2__1 = tmp5;

        tmp24 = evaluate(l3, True, False);
        tmp23 = inv_evaluate(l1, tmp24, False);
        tmp22 = evaluate(self.s1, True, tmp23);
        tmp21 = evaluate(self.s2, True, tmp22);
        tmp31 = inv_evaluate(l3, True, False);
        tmp30 = evaluate(l2, True, tmp31);
        tmp29 = evaluate(l1, tmp30, True);
        tmp28 = evaluate(self.s0, tmp29, tmp31);
        tmp34 = inv_evaluate(l2, True, tmp31);
        tmp33 = evaluate(l1, tmp24, tmp34);
        tmp32 = inv_evaluate(self.s0, tmp24, tmp33);
        tmp27 = evaluate(self.s1, tmp28, tmp32);
        tmp26 = evaluate(self.s2, tmp27, tmp31);
        tmp25 = evaluate(self.s3, tmp26, tmp31);
        tmp20 = inv_evaluate(self.s4, tmp21, tmp25);
        l3__1 = tmp20;

        tmp38 = inv_evaluate(l1, True, False);
        tmp37 = evaluate(self.s1, True, tmp38);
        tmp36 = evaluate(self.s2, True, tmp37);
        tmp43 = evaluate(l1, True, False);
        tmp42 = evaluate(self.s0, tmp43, False);
        tmp46 = evaluate(l3, True, False);
        tmp45 = evaluate(l1, True, tmp46);
        tmp47 = evaluate(l2, True, False);
        tmp44 = evaluate(self.s0, tmp45, tmp47);
        tmp41 = evaluate(self.s1, tmp42, tmp44);
        tmp40 = evaluate(self.s2, tmp41, False);
        tmp39 = inv_evaluate(self.s3, tmp40, False);
        tmp35 = inv_evaluate(self.s4, tmp36, tmp39);
        self.s4 = tmp35;

        tmp54 = evaluate(l3, True, False);
        tmp53 = inv_evaluate(l1, True, tmp54);
        tmp52 = evaluate(self.s0, True, tmp53);
        tmp57 = evaluate(l2, True, False);
        tmp59 = inv_evaluate(l3, True, False);
        tmp58 = evaluate(l2, True, tmp59);
        tmp56 = evaluate(l1, tmp57, tmp58);
        tmp55 = evaluate(self.s0, True, tmp56);
        tmp51 = evaluate(self.s1, tmp52, tmp55);
        tmp61 = evaluate(l1, True, tmp54);
        tmp64 = evaluate(l2, True, tmp54);
        tmp63 = evaluate(l1, True, tmp64);
        tmp62 = evaluate(self.s0, tmp63, tmp61);
        tmp60 = inv_evaluate(self.s1, tmp61, tmp62);
        tmp50 = evaluate(self.s2, tmp51, tmp60);
        tmp67 = evaluate(self.s0, tmp61, tmp63);
        tmp66 = evaluate(self.s1, tmp67, False);
        tmp69 = inv_evaluate(self.s0, tmp57, False);
        tmp68 = inv_evaluate(self.s1, True, tmp69);
        tmp65 = inv_evaluate(self.s2, tmp66, tmp68);
        tmp49 = evaluate(self.s3, tmp50, tmp65);
        tmp48 = inv_evaluate(self.s4, True, tmp49);
        self.s3 = tmp48;

        tmp73 = evaluate(self.s0, True, False);
        tmp74 = inv_evaluate(self.s0, True, False);
        tmp72 = inv_evaluate(self.s1, tmp73, tmp74);
        tmp71 = evaluate(self.s2, True, tmp72);
        tmp80 = evaluate(l3, True, False);
        tmp79 = inv_evaluate(l1, True, tmp80);
        tmp78 = evaluate(self.s0, True, tmp79);
        tmp82 = evaluate(l1, True, tmp80);
        tmp84 = evaluate(l2, True, False);
        tmp86 = inv_evaluate(l3, True, False);
        tmp85 = evaluate(l2, True, tmp86);
        tmp83 = evaluate(l1, tmp84, tmp85);
        tmp81 = evaluate(self.s0, tmp82, tmp83);
        tmp77 = evaluate(self.s1, tmp78, tmp81);
        tmp88 = evaluate(self.s0, tmp82, True);
        tmp91 = evaluate(l2, True, tmp80);
        tmp90 = evaluate(l1, True, tmp91);
        tmp89 = evaluate(self.s0, tmp90, tmp79);
        tmp87 = inv_evaluate(self.s1, tmp88, tmp89);
        tmp76 = evaluate(self.s2, tmp77, tmp87);
        tmp94 = inv_evaluate(self.s0, tmp82, False);
        tmp93 = evaluate(self.s1, True, tmp94);
        tmp96 = inv_evaluate(self.s0, tmp83, True);
        tmp95 = inv_evaluate(self.s1, True, tmp96);
        tmp92 = evaluate(self.s2, tmp93, tmp95);
        tmp75 = evaluate(self.s3, tmp76, tmp92);
        tmp70 = inv_evaluate(self.s4, tmp71, tmp75);
        self.s2 = tmp70;

        tmp101 = evaluate(l1, True, False);
        tmp100 = inv_evaluate(self.s0, tmp101, False);
        tmp99 = evaluate(self.s1, True, tmp100);
        tmp98 = evaluate(self.s2, True, tmp99);
        tmp107 = evaluate(l3, True, False);
        tmp106 = evaluate(l1, True, tmp107);
        tmp105 = evaluate(self.s0, tmp101, tmp106);
        tmp110 = evaluate(l2, True, False);
        tmp112 = inv_evaluate(l3, True, False);
        tmp111 = evaluate(l2, True, tmp112);
        tmp109 = evaluate(l1, tmp110, tmp111);
        tmp108 = inv_evaluate(self.s0, True, tmp109);
        tmp104 = evaluate(self.s1, tmp105, tmp108);
        tmp114 = inv_evaluate(l1, True, tmp107);
        tmp113 = inv_evaluate(self.s0, True, tmp114);
        tmp103 = evaluate(self.s2, tmp104, tmp113);
        tmp118 = inv_evaluate(l2, True, False);
        tmp117 = evaluate(self.s0, True, tmp118);
        tmp119 = inv_evaluate(self.s0, tmp106, False);
        tmp116 = evaluate(self.s1, tmp117, tmp119);
        tmp121 = evaluate(self.s0, tmp106, False);
        tmp122 = inv_evaluate(self.s0, tmp109, tmp118);
        tmp120 = inv_evaluate(self.s1, tmp121, tmp122);
        tmp115 = inv_evaluate(self.s2, tmp116, tmp120);
        tmp102 = inv_evaluate(self.s3, tmp103, tmp115);
        tmp97 = inv_evaluate(self.s4, tmp98, tmp102);
        self.s1 = tmp97;

        tmp129 = evaluate(l2, True, False);
        tmp128 = evaluate(l1, tmp129, False);
        tmp131 = evaluate(l3, True, False);
        tmp130 = evaluate(l1, True, tmp131);
        tmp127 = evaluate(self.s0, tmp128, tmp130);
        tmp135 = inv_evaluate(l3, True, False);
        tmp134 = evaluate(l2, True, tmp135);
        tmp133 = inv_evaluate(l1, tmp129, tmp134);
        tmp132 = evaluate(self.s0, tmp130, tmp133);
        tmp126 = evaluate(self.s1, tmp127, tmp132);
        tmp137 = inv_evaluate(self.s0, tmp129, tmp130);
        tmp136 = inv_evaluate(self.s1, True, tmp137);
        tmp125 = evaluate(self.s2, tmp126, tmp136);
        tmp141 = inv_evaluate(u1, tmp130, False);
        tmp140 = inv_evaluate(self.s0, True, tmp141);
        tmp139 = evaluate(self.s1, tmp132, tmp140);
        tmp144 = evaluate(u1, tmp130, False);
        tmp143 = evaluate(self.s0, tmp130, tmp144);
        tmp148 = evaluate(l2, True, tmp131);
        tmp147 = evaluate(l1, True, tmp148);
        tmp146 = inv_evaluate(u1, tmp147, False);
        tmp145 = inv_evaluate(self.s0, True, tmp146);
        tmp142 = evaluate(self.s1, tmp143, tmp145);
        tmp138 = evaluate(self.s2, tmp139, tmp142);
        tmp124 = inv_evaluate(self.s3, tmp125, tmp138);
        tmp123 = inv_evaluate(self.s4, True, tmp124);
        self.s0 = tmp123;

        return (l1__1, l2__1, l3__1)