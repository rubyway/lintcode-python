"""
寻找峰值

    描述
    笔记
    数据
    评测

你给出一个整数数组(size为n)，其具有以下特点：

    相邻位置的数字是不同的
    A[0] < A[1] 并且 A[n - 2] > A[n - 1]

假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
注意事项

数组可能包含多个峰值，只需找到其中的任何一个即可
您在真实的面试中是否遇到过这个题？
样例

给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.
"""
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        length = len(A)
        left, right = 0, length- 1
        while left<= right:
            mid = (left+ right)>>1
            if left == mid:
                return right if A[left] < A[right] else left
            elif A[mid] < A[mid+ 1]:
                left = mid
            elif A[mid] > A[mid+ 1]:
                right = mid
        return -1
