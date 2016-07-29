def priCom(a, b):
    priMat = [\
#/*  +    -    *    /    ^    !    (    )    #	*/ 横轴为当前运算符，纵轴为栈顶运算符#
    ['>', '>', '<', '<', '<', '<', '<', '>', '>'],\
    ['>', '>', '<', '<', '<', '<', '<', '>', '>',],\
    ['>', '>', '>', '>', '<', '<', '<', '>', '>',],\
    ['>', '>', '>', '>', '<', '<', '<', '>', '>',],\
    ['>', '>', '>', '>', '>', '<', '<', '>', '>',],\
    ['>', '>', '>', '>', '>', '>', ' ', '>', '>',],\
    ['<', '<', '<', '<', '<', '<', '<', '=', ' ',],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],\
    ['<', '<', '<', '<', '<', '<', '<', ' ', '='],\
    ]
    tempDict = {'+':0, '-':1, '*':2, '/':3, '^':4, '!':5, '(':6, ')':7, '#':8}
    return priMat[tempDict[a]][tempDict[b]]
#print priCom('+', '*')
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



def convertToRPN(aList):
    #opnd = []#操作数栈
    rpnd = []#RPN
    opcd = []#操作符栈
    opcd.append('#')
    
    while(opcd != []):
        i = 0
        while i < len(aList):
            if aList[i].isdigit():
                #opnd.append(aList[i])
                rpnd.append(aList[i])
                i += 1
            else:
                pri = priCom(opcd[-1], aList[i])
                if  pri == '<':
                    opcd.append(aList[i])
                    i += 1
                elif pri == '=':
                    opcd.pop()
                    i += 1
                elif pri == '>':
                    opc = opcd.pop()
                    rpnd.append(opc)
        for j in opcd[-1:0:-1]:
            rpnd.append(j)
        break
    return rpnd
#a = ['3', '-', '4', '!', '+', '5']
a = ['(', '1', '+', '2', ')', '*', '(', '2', '-', '1', ')']
print convertToRPN(a)
