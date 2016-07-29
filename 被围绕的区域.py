"""


给一个二维的矩阵，包含 'X' 和 'O', 找到所有被 'X' 围绕的区域，并用 'X' 填充满。
您在真实的面试中是否遇到过这个题？
样例

给出二维矩阵：

X X X X
X O O X
X X O X
X O X X

把被 'X' 围绕的区域填充之后变为：

X X X X
X X X X
X X X X
X O X X

"""
class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        if board == []:
            return []
        row, col = len(board), len(board[0])
        for i in xrange(row):
            if board[i][0] == 'O':
                self.search(board, i, 0)
            if board[i][-1] == 'O':
                self.search(board, i, col- 1)
        for j in xrange(col):
            if board[0][j] == 'O':
                self.search(board, 0, j)
            if board[-1][j] == 'O':
                self.search(board, row- 1, j)
        for m in xrange(row):
            for n in xrange(col):
                if board[m][n] == 'O':
                    board[m][n] = 'X'
                if board[m][n] == '#':
                    board[m][n] = 'O'                    
                    
    def search(self, board, i, j):
        row, col = len(board), len(board[0])
        if i< 0 or j< 0 or i >= row or j >= col:
            return
        if board[i][j] != 'O':
            return
        board[i][j] = '#'
        self.search(board, i- 1, j)
        self.search(board, i+ 1, j)
        self.search(board, i, j- 1)
        self.search(board, i, j+ 1)
