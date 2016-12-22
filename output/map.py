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
    def move(self,l1, l2, l3, l4):
        tmp1 = evaluate(l1, True, False);
        l1__1 = tmp1;

        tmp7 = inv_evaluate(l2, True, False);
        tmp6 = evaluate(l1, True, tmp7);
        tmp9 = evaluate(l2, True, False);
        tmp8 = inv_evaluate(l1, tmp9, False);
        tmp5 = evaluate(self.s0, tmp6, tmp8);
        tmp11 = evaluate(l1, True, tmp9);
        tmp12 = evaluate(l1, tmp9, True);
        tmp10 = inv_evaluate(self.s0, tmp11, tmp12);
        tmp4 = evaluate(self.s1, tmp5, tmp10);
        tmp14 = evaluate(self.s0, tmp12, tmp11);
        tmp16 = evaluate(l1, tmp9, False);
        tmp15 = evaluate(self.s0, tmp9, tmp16);
        tmp13 = inv_evaluate(self.s1, tmp14, tmp15);
        tmp3 = evaluate(self.s2, tmp4, tmp13);
        tmp19 = inv_evaluate(l1, True, tmp7);
        tmp18 = evaluate(self.s1, tmp12, tmp19);
        tmp21 = inv_evaluate(self.s0, True, tmp8);
        tmp20 = evaluate(self.s1, tmp9, tmp21);
        tmp17 = inv_evaluate(self.s2, tmp18, tmp20);
        tmp2 = inv_evaluate(self.s3, tmp3, tmp17);
        l2__1 = tmp2;

        tmp27 = evaluate(l2, True, False);
        tmp26 = inv_evaluate(l1, tmp27, False);
        tmp25 = evaluate(self.s0, True, tmp26);
        tmp31 = evaluate(l3, True, False);
        tmp30 = inv_evaluate(l2, tmp31, True);
        tmp29 = evaluate(l1, True, tmp30);
        tmp34 = inv_evaluate(l3, True, False);
        tmp33 = evaluate(l2, True, tmp34);
        tmp32 = evaluate(l1, tmp33, False);
        tmp28 = inv_evaluate(self.s0, tmp29, tmp32);
        tmp24 = evaluate(self.s1, tmp25, tmp28);
        tmp38 = inv_evaluate(l2, tmp31, False);
        tmp37 = evaluate(l1, True, tmp38);
        tmp36 = inv_evaluate(self.s0, tmp37, True);
        tmp35 = evaluate(self.s1, True, tmp36);
        tmp23 = evaluate(self.s2, tmp24, tmp35);
        tmp42 = evaluate(l1, tmp27, True);
        tmp41 = evaluate(self.s0, True, tmp42);
        tmp43 = inv_evaluate(l1, tmp31, True);
        tmp40 = evaluate(self.s1, tmp41, tmp43);
        tmp47 = inv_evaluate(l2, True, tmp34);
        tmp46 = evaluate(l1, True, tmp47);
        tmp45 = evaluate(self.s0, tmp46, False);
        tmp49 = evaluate(l1, True, tmp34);
        tmp50 = evaluate(l1, tmp33, True);
        tmp48 = inv_evaluate(self.s0, tmp49, tmp50);
        tmp44 = inv_evaluate(self.s1, tmp45, tmp48);
        tmp39 = inv_evaluate(self.s2, tmp40, tmp44);
        tmp22 = evaluate(self.s3, tmp23, tmp39);
        l3__1 = tmp22;

        tmp55 = evaluate(l2, True, False);
        tmp54 = evaluate(l1, tmp55, False);
        tmp53 = inv_evaluate(self.s1, True, tmp54);
        tmp52 = evaluate(self.s2, True, tmp53);
        tmp60 = evaluate(l4, True, False);
        tmp59 = evaluate(l1, True, tmp60);
        tmp62 = inv_evaluate(l4, True, False);
        tmp61 = inv_evaluate(l1, True, tmp62);
        tmp58 = evaluate(self.s0, tmp59, tmp61);
        tmp57 = evaluate(self.s1, tmp58, False);
        tmp66 = evaluate(l2, True, tmp62);
        tmp65 = evaluate(l1, tmp55, tmp66);
        tmp64 = evaluate(self.s0, True, tmp65);
        tmp63 = inv_evaluate(self.s1, tmp64, True);
        tmp56 = evaluate(self.s2, tmp57, tmp63);
        tmp51 = evaluate(self.s3, tmp52, tmp56);
        l4__1 = tmp51;

        tmp72 = inv_evaluate(l2, True, False);
        tmp71 = evaluate(l1, True, tmp72);
        tmp70 = evaluate(self.s0, tmp71, True);
        tmp69 = evaluate(self.s1, True, tmp70);
        tmp76 = evaluate(l2, True, False);
        tmp75 = evaluate(l1, tmp76, True);
        tmp77 = evaluate(l1, True, tmp76);
        tmp74 = evaluate(self.s0, tmp75, tmp77);
        tmp81 = evaluate(l3, True, False);
        tmp80 = inv_evaluate(l2, tmp81, True);
        tmp79 = evaluate(l1, tmp76, tmp80);
        tmp82 = evaluate(l1, tmp76, False);
        tmp78 = inv_evaluate(self.s0, tmp79, tmp82);
        tmp73 = evaluate(self.s1, tmp74, tmp78);
        tmp68 = evaluate(self.s2, tmp69, tmp73);
        tmp86 = evaluate(l1, True, False);
        tmp85 = evaluate(self.s0, tmp86, False);
        tmp87 = inv_evaluate(self.s0, tmp71, True);
        tmp84 = evaluate(self.s1, tmp85, tmp87);
        tmp92 = inv_evaluate(l4, True, False);
        tmp91 = evaluate(l2, True, tmp92);
        tmp90 = inv_evaluate(l1, tmp76, tmp91);
        tmp89 = evaluate(self.s0, tmp82, tmp90);
        tmp88 = evaluate(self.s1, tmp89, False);
        tmp83 = evaluate(self.s2, tmp84, tmp88);
        tmp67 = evaluate(self.s3, tmp68, tmp83);
        self.s3 = tmp67;

        tmp99 = evaluate(l3, True, False);
        tmp98 = evaluate(l2, True, tmp99);
        tmp97 = evaluate(l1, tmp98, True);
        tmp96 = evaluate(self.s0, True, tmp97);
        tmp95 = evaluate(self.s1, True, tmp96);
        tmp103 = evaluate(l2, True, False);
        tmp102 = evaluate(l1, True, tmp103);
        tmp101 = evaluate(self.s0, True, tmp102);
        tmp106 = inv_evaluate(l2, True, False);
        tmp105 = evaluate(l1, True, tmp106);
        tmp104 = evaluate(self.s0, tmp105, True);
        tmp100 = inv_evaluate(self.s1, tmp101, tmp104);
        tmp94 = evaluate(self.s2, tmp95, tmp100);
        tmp110 = evaluate(l1, tmp103, True);
        tmp111 = inv_evaluate(l1, True, False);
        tmp109 = evaluate(self.s0, tmp110, tmp111);
        tmp112 = inv_evaluate(l1, True, tmp103);
        tmp108 = evaluate(self.s1, tmp109, tmp112);
        tmp116 = inv_evaluate(l2, True, tmp99);
        tmp115 = evaluate(l1, True, tmp116);
        tmp114 = evaluate(self.s0, tmp115, tmp105);
        tmp119 = inv_evaluate(l3, True, False);
        tmp118 = evaluate(l1, True, tmp119);
        tmp117 = evaluate(self.s0, tmp118, True);
        tmp113 = inv_evaluate(self.s1, tmp114, tmp117);
        tmp107 = evaluate(self.s2, tmp108, tmp113);
        tmp93 = evaluate(self.s3, tmp94, tmp107);
        self.s2 = tmp93;

        tmp125 = inv_evaluate(l2, True, False);
        tmp124 = evaluate(l1, True, tmp125);
        tmp127 = evaluate(l2, True, False);
        tmp126 = inv_evaluate(l1, tmp127, False);
        tmp123 = evaluate(self.s0, tmp124, tmp126);
        tmp129 = evaluate(l1, True, False);
        tmp132 = inv_evaluate(l3, True, False);
        tmp131 = evaluate(l2, True, tmp132);
        tmp130 = evaluate(l1, tmp131, True);
        tmp128 = inv_evaluate(self.s0, tmp129, tmp130);
        tmp122 = evaluate(self.s1, tmp123, tmp128);
        tmp135 = evaluate(l1, True, tmp127);
        tmp134 = evaluate(self.s0, True, tmp135);
        tmp139 = evaluate(l3, True, False);
        tmp138 = inv_evaluate(l2, tmp139, True);
        tmp137 = evaluate(l1, tmp127, tmp138);
        tmp140 = evaluate(l1, tmp127, False);
        tmp136 = evaluate(self.s0, tmp137, tmp140);
        tmp133 = evaluate(self.s1, tmp134, tmp136);
        tmp121 = evaluate(self.s2, tmp122, tmp133);
        tmp143 = evaluate(self.s0, tmp129, False);
        tmp144 = inv_evaluate(l1, tmp139, tmp127);
        tmp142 = evaluate(self.s1, tmp143, tmp144);
        tmp146 = evaluate(self.s0, tmp135, tmp127);
        tmp149 = evaluate(l2, True, tmp139);
        tmp148 = inv_evaluate(l1, tmp149, False);
        tmp147 = inv_evaluate(self.s0, True, tmp148);
        tmp145 = inv_evaluate(self.s1, tmp146, tmp147);
        tmp141 = inv_evaluate(self.s2, tmp142, tmp145);
        tmp120 = evaluate(self.s3, tmp121, tmp141);
        self.s1 = tmp120;

        tmp153 = evaluate(l1, True, False);
        tmp156 = evaluate(l2, True, False);
        tmp155 = evaluate(l1, True, tmp156);
        tmp154 = evaluate(self.s0, tmp155, tmp153);
        tmp152 = evaluate(self.s1, tmp153, tmp154);
        tmp160 = inv_evaluate(l2, True, False);
        tmp159 = evaluate(l1, True, tmp160);
        tmp158 = evaluate(self.s0, tmp153, tmp159);
        tmp164 = evaluate(l3, True, False);
        tmp163 = evaluate(l2, tmp164, True);
        tmp162 = evaluate(l1, tmp156, tmp163);
        tmp165 = evaluate(l1, tmp156, True);
        tmp161 = inv_evaluate(self.s0, tmp162, tmp165);
        tmp157 = evaluate(self.s1, tmp158, tmp161);
        tmp151 = evaluate(self.s2, tmp152, tmp157);
        tmp170 = evaluate(l4, True, False);
        tmp169 = evaluate(l1, True, tmp170);
        tmp172 = inv_evaluate(l4, True, False);
        tmp171 = inv_evaluate(l1, tmp156, tmp172);
        tmp168 = evaluate(self.s0, tmp169, tmp171);
        tmp167 = evaluate(self.s1, tmp168, tmp159);
        tmp177 = inv_evaluate(l3, True, False);
        tmp176 = inv_evaluate(l2, True, tmp177);
        tmp175 = evaluate(l1, True, tmp176);
        tmp178 = inv_evaluate(l1, tmp156, True);
        tmp174 = evaluate(self.s0, tmp175, tmp178);
        tmp180 = evaluate(l1, True, tmp164);
        tmp179 = evaluate(self.s0, tmp180, tmp178);
        tmp173 = evaluate(self.s1, tmp174, tmp179);
        tmp166 = evaluate(self.s2, tmp167, tmp173);
        tmp150 = evaluate(self.s3, tmp151, tmp166);
        self.s0 = tmp150;

        return (l1__1, l2__1, l3__1, l4__1)