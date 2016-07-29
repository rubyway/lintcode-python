"""


给定一个包含 m x n 个要素的矩阵，（m 行, n 列），按照螺旋顺序，返回该矩阵中的所有要素。
您在真实的面试中是否遇到过这个题？
样例

给定如下矩阵：

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

应返回 [1,2,3,6,9,8,7,4,5]。
"""
class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        row= len(matrix)
        result = []
        if row == 0:
            return []
        col = len(matrix[0]) 
    
        left, right, up, down = 0, col, 0, row
        while left< right and up< down:
            
            for _ in xrange(left, right):
                result.append(matrix[up][_])
                
            for _ in xrange(up+ 1, down):
                result.append(matrix[_][right- 1])
                
            for _ in xrange(right- 2, left- 1, -1):
                if up < down- 1:
                    result.append(matrix[down- 1][_])
                    
            for _ in xrange(down- 2, up, -1):
                if left < right- 1:
                    result.append(matrix[_][left])
                    
            left += 1
            right -= 1
            up += 1
            down -= 1
        return result
