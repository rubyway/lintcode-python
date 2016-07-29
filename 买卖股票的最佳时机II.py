"""


假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。
您在真实的面试中是否遇到过这个题？
样例

给出一个数组样例[2,1,2,0,1], 返回 2
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
    #def maxProfit(prices):
        length = len(prices)
        if length <= 1:
            return 0
        result = 0
        templist = [prices[0]]
        for i in xrange(1, length):
            if prices[i] <= prices[i- 1]:
                result += (templist[-1]- templist[0])
                templist = []
            templist.append(prices[i])
        return result + (templist[-1]- templist[0])
