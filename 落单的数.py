"""
 落单的数

给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例
给出 [1,2,2,1,3,4,3]，返回 4"""
class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        length = len(A)
        if length == 0:
            return 0
        templist = []
        for i in A:
            if i not in templist:
                templist.append(i)
            else:
                templist.remove(i)
        return templist[0]
        
 """
     def singleNumber(self, A):
        length = len(A)
        if length == 0:
            return 0
        result = A[0]
        for i in xrange(1, length):
            result ^= A[i]
        return result"""
