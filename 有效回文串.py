"""
有效回文串
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。
你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。
在这个题目中，我们将空字符串判定为有效回文。
"A man, a plan, a canal: Panama" 是一个回文。
"race a car" 不是一个回文。"""
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        length = len(s)
        if length == 0 or s == ' '*length or length == 1:
            return True
        i, j = 0, length- 1
        while i< length and j> -1:
            while not self.check(s[i]):
                i += 1
                if i >= length:
                    return True
            while not self.check(s[j]):
                j -= 1
                if j<= -1:
                    return True
            if i == j and s[i].lower() == s[j].lower():
                return True
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True  
                   
    def check(self, a):
        if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9'):
            return True
        else:
            return False
