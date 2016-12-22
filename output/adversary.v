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
    def init(self):
        self.s0 = 0;
        self.s1 = 0;
    def move(self,l1, l2, l3):
        tmp1 = evaluate(l1, 1, 0);
        l1__1 = tmp1;

        tmp4 = inv_evaluate(l2, 1, 0);
        tmp3 = evaluate(s0, 1, tmp4);
        tmp2 = inv_evaluate(s1, 1, tmp3);
        l2__1 = tmp2;

        tmp5 = evaluate(l3, 1, 0);
        l3__1 = tmp5;

        tmp7 = inv_evaluate(s0, 1, 0);
        tmp6 = inv_evaluate(s1, 1, tmp7);
        self.s1 = tmp6;

        tmp10 = inv_evaluate(l2, 1, 0);
        tmp9 = evaluate(s0, 1, tmp10);
        tmp8 = inv_evaluate(s1, 1, tmp9);
        self.s0 = tmp8;

        return (l1__1, l2__1, l3__1)