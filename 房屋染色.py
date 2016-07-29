"""
房屋染色

 描述
 笔记
 数据
 评测
这里有n个房子在一列直线上，现在我们需要给房屋染色，分别有红色蓝色和绿色。每个房屋染不同的颜色费用也不同，你需要设计一种染色方案使得相邻的房屋颜色不同，并且费用最小。

费用通过一个nx3 的矩阵给出，比如cost[0][0]表示房屋0染红色的费用，cost[1][2]表示房屋1染绿色的费用。

 注意事项

所有费用都是正整数

样例
costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

房屋 0 蓝色, 房屋 1 绿色, 房屋 2 蓝色， 2 + 5 + 3 = 10"""
class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
    #def minCost(costs):
        length = len(costs)
        if costs == []:
            return 0
        dp = [[0 for i in range(3)] for j in range(length)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]   
        for i in xrange(1, length):
            dp[i][0]  = min(dp[i- 1][1], dp[i- 1][2])+ costs[i][0]
            dp[i][1]  = min(dp[i- 1][0], dp[i- 1][2])+ costs[i][1]
            dp[i][2]  = min(dp[i- 1][0], dp[i- 1][1])+ costs[i][2]
        return min(dp[length- 1])
            
