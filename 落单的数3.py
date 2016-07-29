"""
给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。

样例
给出 [1,2,2,3,4,4,5,3]，返回 1和5

挑战 
O(n)时间复杂度，O(1)的额外空间复杂度"""
"""class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        length = len(A)
        if length == 0:
            return 0
        templist = []
        for i in A:
            if i not in templist:
                templist.append(i)
            else:
                templist.remove(i)
        return templist"""
class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        length = len(A)
        if length == 0:
            return 0
        yihuo = 0
        for i in xrange(length):
            yihuo ^= A[i]
        indexof1 = 0
        for j in xrange(32):
            temp = 1<<j
            if temp & yihuo:
                break
        result = []
        result.extend(self.singleNumberI(temp, A))
        return result
        
    def singleNumberI(self, temp, A):
        re1, re2 = 0, 0
        for i in xrange(len(A)):
            if temp & A[i]:
                re1 ^= A[i]
            else:
                re2 ^= A[i]
        return [re1, re2]
