"""
罗马数字转整数

 描述
 笔记
 数据
 评测
给定一个罗马数字，将其转换成整数。

返回的结果要求在1到3999的范围内。

您在真实的面试中是否遇到过这个题？ Yes
说明
什么是 罗马数字?

https://en.wikipedia.org/wiki/Roman_numerals
https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
http://baike.baidu.com/view/42061.htm
样例
IV -> 4

XII -> 12

XXI -> 21

XCIX -> 99"""
class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
#从前往后判断规则
        length = len(s)
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sums = 0
        if s in dict:
            return dict[s]
        i = 0
        while i< length:
            if i == length- 1:
                sums += dict[s[i]]
            elif dict[s[i]] > dict[s[i+ 1]]:
                sums += dict[s[i]]
            elif dict[s[i]] == dict[s[i+ 1]]:
                sums += dict[s[i]]
            elif dict[s[i]] < dict[s[i+ 1]]:#后减前的情况，i向后两位，循环continue,其余情况i都后移一位
                sums += (dict[s[i+ 1]]- dict[s[i]])
                i += 2
                continue
            i += 1
        return sums
