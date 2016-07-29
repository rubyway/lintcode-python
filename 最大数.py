"""
最大数

给出一组非负整数，重新排列他们的顺序把他们组成一个最大的整数。


最后的结果可能很大，所以我们返回一个字符串来代替这个整数。

样例
给出 [1, 20, 23, 4, 8]，返回组合最大的整数应为8423201。"""
###https://docs.python.org/2/howto/sorting.html#sortinghowto
class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        length = len(num)
        if num == [0]*length:
            return '0'
        tempstr = ''
        num = sorted([str(i) for i in num], cmp = self.helper, reverse=True)
        for i in num:
            tempstr += i
        return tempstr

    def helper(self, x, y):
        if (x + y) > (y + x):
            return 1
        else:
            return -1
