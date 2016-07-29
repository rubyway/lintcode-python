"""最多有多少个点在一条直线上

给出二维平面上的n个点，求最多有多少点在同一条直线上。

样例
给出4个点：(1, 2), (3, 6), (0, 0), (1, 3)。

一条直线上的点最多有3个。"""
#http://bookshadow.com/weblog/2014/10/16/leetcode-max-points-line/
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def thesame(self, m, n):
        return m.x == n.x and m.y == n.y
    def kk(self, p, q):
        if p.x == q.x:
            return None
        else:
            return 1.0*(p.y- q.y)/(p.x- q.x)
    def maxPoints(self, points):
        length = len(points)
        maxnum =0
        for i in xrange(length):
            tempdict = {}
            temp  = 0
            for j in xrange(i+ 1, length):
                if self.thesame(points[i], points[j]):
                    temp += 1
                else:
                    k = self.kk(points[i], points[j])
                    if tempdict.get(k) is None:
                        tempdict[k] = 1
                    else:
                        tempdict[k] += 1
            value = 0
            if len(tempdict):
                value = max(tempdict.values())
            maxnum = max(maxnum,  value+ temp+ 1)
        return maxnum
