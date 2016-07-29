"""


给定一个N×N的二维矩阵表示图像，90度顺时针旋转图像。


您在真实的面试中是否遇到过这个题？
样例

给出一个矩形[[1,2],[3,4]]，90度顺时针旋转后，返回[[3,1],[4,2]]
挑战

能否在原地完成？
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n/2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        for i in xrange(n):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
