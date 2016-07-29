"""
给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的1/k。

 注意事项

数组中只有唯一的主元素

样例
给出数组 [3,1,2,3,2,3,3,4,4,4] ，和 k = 3，返回 3"""
class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        length = len(nums)
        tempdict = {}
        for i in nums:
            if i not in tempdict:
                tempdict[i] = 1
            else:
                tempdict[i] += 1
        temp = sorted(tempdict.items(), key=lambda d: d[1], reverse=True)
        if temp[0][1] < length/ k:
            return 0
        elif temp[0][1] > length/ k:
            return temp[0][0]
        
