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
    def move(self,l1, l2, l3):
        tmp1 = evaluate(l1, True, False);
        l1__1 = tmp1;

        tmp4 = inv_evaluate(l2, True, False);
        tmp3 = evaluate(self.s0, True, tmp4);
        tmp2 = inv_evaluate(self.s1, True, tmp3);
        l2__1 = tmp2;

        tmp5 = evaluate(l3, True, False);
        l3__1 = tmp5;

        tmp7 = inv_evaluate(self.s0, True, False);
        tmp6 = inv_evaluate(self.s1, True, tmp7);
        self.s1 = tmp6;

        tmp10 = inv_evaluate(l2, True, False);
        tmp9 = evaluate(self.s0, True, tmp10);
        tmp8 = inv_evaluate(self.s1, True, tmp9);
        self.s0 = tmp8;

        return (l1__1, l2__1, l3__1)