"""


给定一个m×n矩阵，如果一个元素是0，则将其所在行和列全部元素变成0。

需要在原矩阵上完成操作。
您在真实的面试中是否遇到过这个题？
样例

给出一个矩阵

[
  [1, 2],
  [0, 3]
]

返回

[
  [0, 2],
  [0, 0]
]

"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        if matrix == []:
            return []
        rows, cols = len(matrix), len(matrix[0])
        zeropos = []
        for i in xrange(rows):
            for j in xrange(cols):
                if matrix[i][j] == 0:
                    zeropos.append((i, j))
        if zeropos == []:
            return matrix
        for k in zeropos:
            matrix[k[0]] = [0]*cols#row to 0
            for l in xrange(rows):
                matrix[l][k[1]] = 0
        return matrix
