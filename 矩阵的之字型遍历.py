"""


给你一个包含 m x n 个元素的矩阵 (m 行, n 列), 求该矩阵的之字型遍历。
您在真实的面试中是否遇到过这个题？
样例

对于如下矩阵：

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]

返回 [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
"""
class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        row = len(matrix)
        result = []
        if row == 0:
            return None
        if row == 1:
            return matrix[0]
        col = len(matrix[0])
        if col == 1:
            for i in xrange(row):
                result.append(matrix[i][0])
            return result
            
        length = row* col

        result.append(matrix[0][0])
        i, j = 0, 0
        while i< row and j< col:
            #right
            if (j+ 1)< col:
                result.append(matrix[i][j+ 1])
                j += 1
            #down
            elif (i+ 1)< row:
                result.append(matrix[i+ 1][j])
                i += 1
                
            #downleft
            while (i+ 1)< row and (j- 1)> -1:
                result.append(matrix[i+ 1][j- 1])
                i += 1
                j -= 1
                
            #down
            if (i+ 1)< row:
                result.append(matrix[i+ 1][j])
                i += 1
            #right
            elif (j+ 1)< col:
                result.append(matrix[i][j+ 1])
                j += 1
            
            #upright
            while (i- 1)> -1 and (j+ 1)< col:
                result.append(matrix[i- 1][j+ 1])
                i -= 1
                j += 1
            if i == row- 1 and j == col- 1:
                break
        return result
