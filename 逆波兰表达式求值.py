def cal2(a, op, b):
    if op == '+':
        return float(a) + float(b)
    elif op == '-':
        return float(a) - float(b)
    elif op == '*':
        return float(a) * float(b)
    elif op == '/':
        if 0 == b:
            return 0
        else:
            return float(a) / float(b)
    elif op == '^':
        return float(a)**float(b)
        
fab = lambda x: x*fab(x-1) if x > 1 else 1

def calRPN(aList):
    opnd = []#操作数栈
    for i in aList:
        if i.isdigit():
            opnd.append(i)
        else:
            if '!'== i:
                opn1 = opnd.pop()
                opnd.append(fab(float(opn1)))
            else:
                opn2 = opnd.pop()
                opn3 = opnd.pop()
                opnd.append(cal2(opn3, i, opn2))                    
                
    return opnd                        
a = ['1', '2', '+', '2', '1', '-', '*']                         
print calRPN(a)    
    
    
