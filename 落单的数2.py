"""
给出3*n + 1 个的数字，除其中一个数字之外其他每个数字均出现三次，找到这个数字。

您在真实的面试中是否遇到过这个题？ Yes
样例
给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4"""
class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        length = len(A)
        tempdict = {}
        if length == 0:
            return 0
        for i in A:
            if i not in tempdict:
                tempdict[i] = 1
            else:
                tempdict[i] += 1
        return sorted(tempdict.items(), key = lambda x: x[1])[0][0]
"""
class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        length = len(A)
        if length == 0:
            return 0
        result = [0]*32
        for i in xrange(length):
            for j in xrange(32):
                result[j] = (result[j] + ((A[i]>>j) & 1))%3
        temp = 0
        for k in xrange(32):
            temp += result[k]*(2**k)
        return temp
        """
