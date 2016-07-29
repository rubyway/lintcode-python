"""


分割一个整数数组，使得奇数在前偶数在后。
您在真实的面试中是否遇到过这个题？
样例

给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。
挑战

在原数组中完成，不使用额外空间。
"""

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        length = len(nums)
        if length <= 1:
            return nums
            
        i, j = 0, length-1 
        while i< length or j> -1:
            if nums[i]% 2 != 0:
                i += 1
            
            if nums[j]% 2 == 0:
                j -= 1 
            if i> j:
                break            
            if nums[i]% 2 == 0 and nums[j]% 2 != 0:
                nums[i],  nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            
        return nums
