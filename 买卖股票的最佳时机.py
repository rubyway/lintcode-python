"""
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。

样例
给出一个数组样例 [3,2,3,1,2], 返回 1 """
#减小复杂度的关键在于扫描的同时保存截至目前的最小值
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
        tempmin = prices[0]
        tempdiff = 0
        for i in xrange(1,length):
            if prices[i] <= tempmin:
                tempmin = prices[i]
                continue
            else:
                diff = prices[i] - tempmin
                if diff > tempdiff:
                    tempdiff = diff
        return tempdiff
"""    #def maxProfit(prices):
        tempmax = 0
        for i in xrange(1, len(prices)):
            temp = prices[i]- min(prices[:i])
            if temp > tempmax:
                tempmax = temp
        return tempmax"""
