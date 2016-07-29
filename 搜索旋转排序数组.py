"""假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

样例
给出[4, 5, 1, 2, 3]和target=1，返回 2

给出[4, 5, 1, 2, 3]和target=0，返回 -1"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        length = len(A)
        if length == 0:
            return -1
        return self.helper(A, target, 0, length- 1)
    def helper(self, A, target, left, right):
        middle = (left+ right) >> 1
        if A[middle] == target:
            return middle
        while left < right:
            if A[middle] > A[left]:
                if target >= A[left] and target <= A[middle]:
                    return self.helper(A, target, left, middle- 1)
                else:
                    return self.helper(A, target, middle+ 1, right)
            else:
                if target >= A[middle] and target <= A[right]:
                    return self.helper(A, target, middle+ 1, right)
                else:
                    return self.helper(A, target, left, middle- 1)
        return -1
                    
