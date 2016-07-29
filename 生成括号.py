'''给定 n 对括号，请写一个函数以将其生成新的括号组合，并返回所有组合结果。

样例
给定 n = 3, 可生成的组合如下:

"((()))", "(()())", "(())()", "()(())", "()()()"
http://pythontutor.com/visualize.html#mode=edit'''
def allIter(aStr, solution, n, left, right):
    if len(aStr) == 2*n:
        solution.append(aStr)
    if left < n:
        allIter(aStr+'(', solution, n, left+ 1, right)
    if right < left:
        allIter(aStr+')', solution, n, left, right+ 1)  
    return solution      
def genparen(n):
    solution = []
    allIter('', solution, n, 0, 0)
    return solution
print genparen(3)    
