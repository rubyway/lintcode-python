"""


给定一个整数数组，找出两个 不重叠 子数组使得它们的和最大。
每个子数组的数字在数组中的位置应该是连续的。
返回最大的和。
注意事项

子数组最少包含一个数
您在真实的面试中是否遇到过这个题？
样例

给出数组 [1, 3, -1, 2, -1, 2]
这两个子数组分别为 [1, 3] 和 [2, -1, 2] 或者 [1, 3, -1, 2] 和 [2]，它们的最大和都是 7
挑战

要求时间复杂度为 O(n)
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        length = len(nums)
        if length == 0:
            return None
        dp = [[min(nums)]*length for _ in xrange(2)]
        dp[0][0], dp[1][-1] = nums[0], nums[-1]
        leftmax, rightmax = [nums[0]]* length, [nums[-1]]*length
        result = min(nums)*2
        for i in xrange(1, length):
            dp[0][i] = max(0, dp[0][i- 1])+ nums[i]
            leftmax[i] = max(leftmax[i- 1], dp[0][i])
            
        for j in xrange(length- 2, -1, -1):
            dp[1][j] = max(0, dp[1][j+ 1])+ nums[j]
            rightmax[j] = max(rightmax[j+ 1], dp[1][j])
            
        for k in xrange(length- 1):
            result = max(result, leftmax[k]+ rightmax[k+ 1])
        
        return result
            
            
            
             
