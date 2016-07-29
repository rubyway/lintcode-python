"""


组给出两个整数n和k，返回从1......n中选出的k个数的组合。
您在真实的面试中是否遇到过这个题？
样例

例如 n = 4 且 k = 2

返回的解为：

[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
"""
class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):
        if n == 0 or k == 0:
            return []
        if n == 1 and k == 1:
            return [[n]]
        alist = range(1, n+ 2)
        result = []
        
        def search(a, short, temp):
            length = len(a)
            if k == 0:
                return
            if length == 0:
                return
            if len(temp) == k:
                result.append(temp)
                return
            for i in xrange(length):
                search(a[i+ 1:], short- 1, temp+[a[i]])
        search(alist, k, [])
        return result
