"""
编辑距离

给出两个单词word1和word2，计算出将word1 转换为word2的最少操作次数。

你总共三种操作方法：

    插入一个字符
    删除一个字符
    替换一个字符

给出 work1="mart" 和 work2="karma"

返回 3
"""
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        if length1 == 0 and length2 == 0:
            return 0
        if length1 == 0 and length2 != 0:
            return length2
        if length1 != 0 and length2 == 0:
            return length1
        length1, length2 = len(word1)+ 1, len(word2)+ 1
        dp = [[0 for col in range(length2)] for row in range(length1)]
        for i in xrange(length1):
            dp[i][0] = i
        for i in xrange(length2):
            dp[0][i] = i
        for i in xrange(1, length1):
            temp1 = word1[i- 1]
            for j in xrange(1, length2):
                temp2 = word2[j- 1]
                if temp1 == temp2:
                    dp[i][j] = dp[i- 1][j- 1]
                else: 
                    dp[i][j] = min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))+1;  
        return dp[length1- 1][length2- 1]
