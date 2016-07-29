"""


给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]
您在真实的面试中是否遇到过这个题？
样例

给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]
"""
#O(n)
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
    #def searchRange(A, target):
        length = len(A)
        if length == 0:
            return [-1, -1]
        i = 0
        result = []
        while i< length:
            if A[i] == target:
                result.append(i)
            i += 1
        if result:
            return [result[0], result[-1]]
        else:
            return [-1, -1]
        
