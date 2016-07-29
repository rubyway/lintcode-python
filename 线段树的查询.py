"""


对于一个有n个数的整数数组，在对应的线段树中, 根节点所代表的区间为0-n-1, 每个节点有一个额外的属性max，值为该节点所代表的数组区间start到end内的最大值。

为SegmentTree设计一个 query 的方法，接受3个参数root, start和end，线段树root所代表的数组中子区间[start, end]内的最大值。
注意事项

在做此题之前，请先完成 线段树构造 这道题目。
您在真实的面试中是否遇到过这个题？
样例

对于数组 [1, 4, 2, 3], 对应的线段树为：

                  [0, 3, max=4]
                 /             \
          [0,1,max=4]        [2,3,max=3]
          /         \        /         \
   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]

query(root, 1, 1), return 4

query(root, 1, 2), return 4

query(root, 2, 3), return 3

query(root, 0, 2), return 4
"""
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        if root is None:
            return None
        if (start > end) or (start > root.end) or (end < root.start):
            return None
        if start<= root.start and end>= root.end:
            return root.max
        mid = (root.end+ root.start) >> 1
        return max(self.query(root.left, start, min(mid, end)), self.query(root.right, max(mid, start), end))
            
