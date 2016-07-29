"""
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

样例
括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。"""
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        length = len(s)
        stack = []
        #if (s[0] == ')') or (s[0] == ']') or (s[0] == '}'):
        #    return False
        for i in s:
            if stack == [] and  ((i == ')') or (i == ']') or (i == '}')): 
                return False
            if (i == '(') or (i == '[') or (i == '{'):
                stack.append(i)
            else:
                temp = stack[-1]
                if (temp == '(' and i == ')') or (temp == '[' and i == ']') or (temp == '{' and i =='}'):
                    stack.pop()
                else:
                    stack.append(i)
        if stack == []:
            return True
        else:
            return False
