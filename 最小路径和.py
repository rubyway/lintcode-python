"""
给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。

你在同一时间只能向下或者向右移动一步
"""
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0 for x in xrange(n)] for y in xrange(m)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i- 1][0]+ grid[i][0]
        for j in xrange(1, n):
            dp[0][j] = dp[0][j- 1]+ grid[0][j]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i- 1][j], dp[i][j- 1])+ grid[i][j]
        return dp[-1][-1]
