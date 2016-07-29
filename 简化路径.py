"""
给定一个文档(Unix-style)的完全路径，请进行路径简化。

您在真实的面试中是否遇到过这个题？ Yes
样例
"/home/", => "/home"

"/a/./b/../../c/", => "/c"

挑战 
你是否考虑了 路径 = "/../" 的情况？

在这种情况下，你需返回"/"。

此外，路径中也可能包含双斜杠'/'，如 "/home//foo/"。

在这种情况下，可忽略多余的斜杠，返回 "/home/foo"。"""
class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        length = len(path)
        if length == 0:
            return None
        temp = path.split('/')
        stack = []
        for i in temp:
            if (i == '.') or (len(i) == 0):
                continue
            elif i == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(i)
        result = ''
        if len(stack) == 0:
            return '/'
        for j in stack:
            result += '/'+ j
        return result
