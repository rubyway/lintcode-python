"""


给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）
注意事项

time
您在真实的面试中是否遇到过这个题？
样例

给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.

给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.
"""
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
    #def longestIncreasingContinuousSubsequence(A):
        length = len(A)
        if length == 0:
            return 0
        dps = [0]*length
        dps[0] = 1
        dpj = [0]*length
        dpj[0] = 1
        for i in xrange(1, length):
            if A[i] > A[i- 1]:
                dps[i] = dps[i- 1]+ 1
            elif A[i] < A[i- 1]:
                dps[i] = 1
        for i in xrange(1, length):
            if A[i] < A[i- 1]:
                dpj[i] = dpj[i- 1]+ 1
            elif A[i] > A[i- 1]:
                dpj[i] = 1
        return max(max(dps), max(dpj))      
