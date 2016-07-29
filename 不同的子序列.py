class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        lens, lent = len(S), len(T)
        if lens< lent:
            return 0
        if lent == 0:
            return 1
        dp = [[0 for _ in xrange(lent+ 1)]for _ in xrange(lens+ 1)]
        dp[0][0] = 1
        for i in xrange(lens+ 1):
            dp[i][0] = 1
        for i in xrange(1, lens+ 1):
            for j in xrange(1, lent+ 1):
                if S[i- 1] != T[j- 1]:
                    dp[i][j] = dp[i- 1][j]
                else:
                    dp[i][j] = dp[i- 1][j- 1]+ dp[i- 1][j]
        return dp[-1][-1]
        