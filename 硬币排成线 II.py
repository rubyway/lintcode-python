"""
有 n 个不同价值的硬币排成一条线。两个参赛者轮流从左边依次拿走 1 或 2 个硬币，直到没有硬币为止。计算两个人分别拿到的硬币总价值，价值高的人获胜。

请判定 第一个玩家 是输还是赢？

您在真实的面试中是否遇到过这个题？ Yes
样例
给定数组 A = [1,2,2], 返回 true.

给定数组 A = [1,2,4], 返回 false.
"""
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        length = len(values)
        if length <= 2:
            return True
        dp = [0]*(length+ 1)
        dp[length- 1] = values[-1]
        dp[length- 2] = values[-1]+ values[-2]
        dp[length- 3] = values[-2]+ values[-3]
        for i in xrange(length- 4, -1, -1):
            dp[i] = max(min(dp[i+ 2], dp[i+ 3])+ values[i], min(dp[i+ 3], dp[i+ 4])+ values[i]+ values[i+ 1])
        return dp[0] > (sum(values) - dp[0]) 
