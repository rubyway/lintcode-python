"""
主元素

给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。

样例
给出数组[1,1,1,1,2,2,2]，返回 1

挑战 
要求时间复杂度为O(n)，空间复杂度为O(1)"""
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        length = len(nums)
        tempdict = {}
        for i in nums:
            if i not in tempdict:
                tempdict[i] = 1
            else:
                tempdict[i] += 1
        #sorted(tempdict.items(), key=lambda d: d[1])
        return sorted(tempdict.items(), key=lambda d: d[1], reverse=True)[0][0]
