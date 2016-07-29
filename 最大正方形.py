"""


在一个二维01矩阵中找到全为1的最大正方形
您在真实的面试中是否遇到过这个题？
样例

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

返回 4
"""
class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])

        dp = [[0 for i in xrange(col)] for j in xrange(row)]
        tempmax = 0
        for i in xrange(row):
            for j in xrange(col):
                dp[i][j] = matrix[i][j]
                if dp[i][j] and i>0 and j>0:
                    dp[i][j] = min(dp[i- 1][j- 1], dp[i- 1][j], dp[i][j- 1])+ 1
                tempmax = max(tempmax, dp[i][j])
        return tempmax*tempmax
                    
                    
                
                
