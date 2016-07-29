"""
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。

你可以假设在数组中无重复元素。

您在真实的面试中是否遇到过这个题？ Yes
样例
[1,3,5,6]，5 → 2

[1,3,5,6]，2 → 1

[1,3,5,6]， 7 → 4

[1,3,5,6]，0 → 0"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        length = len(A)
        if length == 0:
            return 0
        low, high = 0, length- 1
        if target< A[0]:
            return 0
        if target> A[-1]:
            return length
        while low<= high:
            mid = (low+ high)>> 1
            if (high- low) == 1 and target> A[low] and target< A[high]:
                return low+ 1
            elif (high- low) == 1 and target== A[low]:
                return low
            elif (high- low) == 1 and target== A[high]:
                return high
            if target > A[mid]:
                low = mid
            elif target < A[mid]:
                high = mid
            elif target == A[mid]:
                return mid
            
        
