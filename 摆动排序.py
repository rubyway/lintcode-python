"""
摆动排序

给你一个没有排序的数组，请将原数组就地重新排列满足如下性质

nums[0] <= nums[1] >= nums[2] <= nums[3]....
 注意事项

请就地排序数组，也就是不需要额外数组

样例
给出数组为 nums = [3, 5, 2, 1, 6, 4] 一种输出方案为 [1, 6, 2, 5, 3, 4]"""
#bookshadow的解法
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        #import copy
        nums.sort()
        #temp = copy.copy(nums)
        temp = nums[:]
        length = len(nums)
        templist = []
        for i in range(1, length, 2) + range(0, length, 2):
            nums[i] = temp.pop()
#不原址排序，带返回的实现
def wiggleSort(nums):
        #import copy
    nums.sort()
    #temp = copy.copy(nums)
    temp = nums[:]
    length = len(nums)
    templist = []
    for i in xrange(length/2):
        nums.append(temp[i])
        nums.append(temp[length- i- 1])
    nums = nums[length:]
    return nums
a = [1,4,2,3,6,5]
wiggleSort(a)
