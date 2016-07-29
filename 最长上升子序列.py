"""
给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

您在真实的面试中是否遇到过这个题？ Yes
说明
最长上升子序列的定义：

最长上升子序列问题是在一个无序的给定序列中找到一个尽可能长的由低到高排列的子序列，这种子序列不一定是连续的或者唯一的。
https://en.wikipedia.org/wiki/Longest_increasing_subsequence

样例
给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3
给出 [4,2,4,5,3,7]，LIS 是 [4,4,5,7]，返回 4
"""
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        length = len(nums)
        if length <= 1:
            return length
        dp = [1]*length
        dp[0] = 1
        tempmax = 1
        for i in xrange(1, length):
            #for j in xrange(1, i):
            j = 0
            temp = 0
            while j< i:
                if nums[j]<= nums[i] and dp[j]> temp:
                    temp = dp[j]
                    dp[i] =  + 1
                    tempmax = max(tempmax, dp[i])
                j += 1
        return tempmax
    
