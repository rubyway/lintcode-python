"""
返回两个数组的交

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2]."""
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))
"""
计算两个数组的交

 注意事项

每个元素出现次数得和在数组里一样
答案可以以任意顺序给出

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2]."""
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        temp = list(set(nums1).intersection(set(nums2)))
        dict1, dict2 = self.todict(nums1), self.todict(nums2)
        templist = []
        for i in temp:
            if dict1[i] <= dict2[i]:
                templist.extend([i]*dict1[i])
            else:
                templist.extend([i]*dict2[i])
        return templist
        
        
    def todict(self, a):
        tempdict = {}
        for i in a:
            if i not in tempdict:
                tempdict[i] = 1
            else:
                tempdict[i] += 1
        return tempdict
