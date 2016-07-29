"""


有 N 个小孩站成一列。每个小孩有一个评级。

按照以下要求，给小孩分糖果：

    每个小孩至少得到一颗糖果。

    评级越高的小孩可以得到更多的糖果。

需最少准备多少糖果？
您在真实的面试中是否遇到过这个题？
样例

给定评级 = [1, 2], 返回 3.

给定评级 = [1, 1, 1], 返回 3.

给定评级 = [1, 2, 2], 返回 4. ([1,2,1]).
"""
class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
    def candy(self, ratings):
        length = len(ratings)
        candy = [1]*length
        for i in xrange(1, length):
            if ratings[i] > ratings[i- 1]:
                candy[i] = candy[i- 1] + 1
        for j in xrange(length-2, -1, -1):
            if ratings[j] > ratings[j+ 1]:
                candy[j] = max(candy[j], candy[j+ 1]+ 1)
        return sum(candy)
