"""


用 O(1) 时间检测整数 n 是否是 2 的幂次。
注意事项

O(1) 时间复杂度
您在真实的面试中是否遇到过这个题？
样例

n=4，返回 true;

n=5，返回 false.

"""

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n == 0:
            return False
        return n&(n- 1) == 0
"""
        temp = bin(n)
        #temp = temp[2:]
        length = len(temp)
        return temp[:3] == '0b1' and temp[3:] == '0'*(length- 3)"""
