"""
给出一个包含 0 .. N 中 N 个数的序列，找出0 .. N 中没有出现在序列中的那个数。


可以改变序列中数的位置。

样例
N = 4 且序列为 [0, 1, 3] 时，缺失的数为2。"""
class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        length = len(nums)
        return length*(length+ 1)/2 - sum(nums)
