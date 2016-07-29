"""
 两个字符串是变位词

    描述
    笔记
    数据
    评测

写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。
您在真实的面试中是否遇到过这个题？
样例

给出 s = "abcd"，t="dcab"，返回 true.
给出 s = "ab", t = "ab", 返回 true.
给出 s = "ab", t = "ac", 返回 false.
"""
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        lengths, lengtht = len(s), len(t)
        if lengths != lengtht:
            return False
        elif lengths == 0 and lengtht == 0:
            return True
        dicts, dictt = {}, {}
        for i in s:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1
        for j in t:
            if j not in dictt:
                dictt[j] = 1
            else:
                dictt[j] += 1
        if dicts == dictt:
            return True
        else:
            return False
