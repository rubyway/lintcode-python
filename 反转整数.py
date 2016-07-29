"""
将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。


给定 x = 123，返回 321

给定 x = -123，返回 -321"""
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        nn = abs(n)
        tempstr = str(nn)
        length = len(tempstr)
        if length == 1:
            return nn if n >= 0 else -nn
        reversestr = tempstr[::-1]
        if int(reversestr) < 2**31:
            return int(reversestr) if n> 0 else -int(reversestr)
        else:
            return 0
