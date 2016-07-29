"""
丢失的第一个正整数

给出一个无序的正数数组，找出其中没有出现的最小正整数。

样例
如果给出 [1,2,0], return 3
如果给出 [3,4,-1,1], return 2

挑战 
只允许时间复杂度O(n)的算法，并且只能使用常数级别的空间。"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        if length == 0:
            return 1
        mina, maxa = min(A), max(A)
        if mina == 1 and length == 1:
            return 2
        if mina > 1 or maxa <= 0:
            return 1
        tempdict = {}
        for i in xrange(1, maxa+ 2):
            tempdict[i] = 0
        for j in A:
            if j > 0:
                if j not in tempdict:
                    tempdict[j] = 1
                else:
                    tempdict[j] += 1
        for (k, v) in tempdict.items():
            if v == 0:
                return k
