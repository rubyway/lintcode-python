"""
数字三角形


给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。
注意事项

如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。

样例

比如，给出下列数字三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
"""
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        import copy
        length = len(triangle)
        dp = copy.deepcopy(triangle)
        for i in xrange(1, length):
            templength = len(triangle[i])
            for j in xrange(templength):
                if j == 0:
                    dp[i][j] = dp[i- 1][0]+ triangle[i][j]
                    continue
                elif j == templength- 1:
                    dp[i][j] = dp[i- 1][-1]+ triangle[i][j]
                    continue
                else:
                    dp[i][j] = min(dp[i- 1][j- 1], dp[i- 1][j]) + triangle[i][j]
        return min(dp[-1])
                
