class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        len1, len2 = len(s1), len(s2)
        if (len1+ len2) != len(s3):
            return False
        if len1 == 0 and len2 != 0:
            if s2 == s3:
                return True
            else:
                return False
        if len2 == 0 and len1 != 0:
            if s1 == s3:
                return True
            else:
                return False        
        dp = [[False] * (len2+ 1) for i in range (len1+ 1)]
        dp[0][0] = True        
        for i in xrange(1, len1+ 1):
            if s1[i- 1] == s3[i- 1]:
                dp[i][0] = dp[i- 1][0]
        for i in xrange(1, len2+ 1):
            if s2[i- 1] == s3[i- 1]:
                dp[0][i] = dp[0][i- 1]

        
        for i in xrange(1, len1+ 1):
            for j in xrange(1, len2+ 1):
                dp[i][j] = ((s1[i- 1] == s3[i+ j- 1]) and dp[i- 1][j]) or ((s2[j- 1] == s3[i+ j- 1]) and dp[i][j- 1])
        return dp[-1][-1]
                
                
                