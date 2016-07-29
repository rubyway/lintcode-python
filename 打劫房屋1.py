"""
假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

您在真实的面试中是否遇到过这个题？ Yes
样例
给定 [3, 8, 4], 返回 8."""
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        lenOfA = len(A)
        if lenOfA == 0:
            return 0
        elif lenOfA == 1:
            return A[0]
        elif lenOfA == 2:
            return max(A[0], A[1])
        #value after robb this house you will get value
        value = [0]*lenOfA
        value[0] = A[0]
        value[1] = A[1]
        value[2] = A[0]+ A[2]
        for i in xrange(3, lenOfA):
            value[i] = A[i] + max(value[i- 2], value[i- 3])#打劫i得到的最大value
        return max(value[lenOfA- 1], value[lenOfA- 2])#最大value必然存在于最后两个其中之一
            
