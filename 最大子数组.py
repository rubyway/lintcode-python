"""


给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
注意事项

子数组最少包含一个数
您在真实的面试中是否遇到过这个题？
样例

给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        length = len(nums)
        if length <= 1:
            return sum(nums)
        dp = [min(nums)]*length
        dp[0] = nums[0]
        tempmax = nums[0]
        for i in xrange(1, length):
            #if dp[i- 1] < 0:
            #    dp[i] = nums[i]
            #else:
            #    dp[i] = dp[i- 1]+ nums[i]
            dp[i] = max(0, dp[i- 1])+ nums[i]
            if dp[i] > tempmax:
                tempmax = dp[i]
        return tempmax        
    
