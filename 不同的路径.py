"""
http://www.lintcode.com/zh-cn/problem/unique-paths/
不同的路径

有一个机器人的位于一个M×N个网格左上角（下图中标记为'Start'）。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角（下图中标记为'Finish'）。
问有多少条不同的路径？
 注意事项

n和m均不超过100

3,7
以上3 x 7的网格中，有多少条不同的路径？"""
#重点在初始化过程
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        a = [1] + [0]*(n- 1)
        dp = [a for j in xrange(m)]
        dp[0] = [1]*n
        dp[0][0] = 0

        
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i][j- 1] + dp[i- 1][j]
        return dp[-1][-1]
