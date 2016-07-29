"""
给出一个二维的字母板和一个单词，寻找字母板网格中是否存在这个单词。

单词可以由按顺序的相邻单元的字母组成，其中相邻单元指的是水平或者垂直方向相邻。每个单元中的字母最多只能使用一次。

您在真实的面试中是否遇到过这个题？ Yes
样例
给出board =

[

  "ABCE",

  "SFCS",

  "ADEE"

]

word = "ABCCED"， ->返回 true,

word = "SEE"，-> 返回 true,

word = "ABCB"， -> 返回 false."""
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        if n == 0:
            return False
        visited = [[False for i in xrange(m)] for j in xrange(n)]
        
        def dfs(i, j, word):
            if len(word) == 0:
                return True
            if i >0 and not visited[i-1][j] and board[i-1][j] == word[0]:
                visited[i-1][j] = True
                if dfs(i-1, j, word[1:]):
                    return True
                visited[i-1][j] = False
            if j>0 and not visited[i][j-1] and board[i][j-1] == word[0]:
                visited[i][j-1] = True
                if dfs(i, j-1, word[1:]):
                    return True
                visited[i][j-1] = False                
            if i+1 <n and not visited[i+1][j] and board[i+1][j] == word[0]:
                visited[i+1][j] = True
                if dfs(i+1, j, word[1:]):
                    return True
                visited[i+1][j] = False
            if j+1 < m and not visited[i][j+1] and board[i][j+1] == word[0]:
                visited[i][j+1] = True
                if dfs(i, j+1, word[1:]):
                    return True
                visited[i][j+1] = False  
            return False
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, word[1:]):
                        return True
                    visited[i][j] = False
        return False
                
                
                
                
       
   
