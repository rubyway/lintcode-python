"""


给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。
注意事项

如果在source中没有这样的子串，返回""，如果有多个这样的子串，返回起始位置最小的子串。
您在真实的面试中是否遇到过这个题？
说明

在答案的子串中的字母在目标字符串中是否需要具有相同的顺序？

——不需要。
样例

给出source = "ADOBECODEBANC"，target = "ABC" 满足要求的解  "BANC"
"""
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        length = len(source)
        if length == 0:
            return ''
        find = 0
        window = [0, length+ 1]
        src = [0]*256
        tar = [0]*256
        for i in target:
            tar[ord(i)] += 1
        begin = 0
        for end in xrange(1, length+ 1):
            temp = source[end- 1]
            if tar[ord(temp)] != 0: src[ord(temp)] += 1 
            if (tar[ord(temp)]> 0 and src[ord(temp)] <= tar[(ord(temp))]): find += 1 

            if find == len(target):
            #将开头字母后续出现的删掉，字符出现次数超过了目标串中出现的次数，并把它们出现次数都减1
                while src[ord(source[begin])] > tar[ord(source[begin])] or tar[ord(source[begin])] == 0:
                    if tar[ord(source[begin])]> 0: src[ord(source[begin])] -= 1 
                    begin += 1
                if (window[1]- window[0]) > (end- begin):
                    window[0], window[1] = begin, end
        
        if window[1] == length+ 1:
            return ''
        else:
            return source[window[0]: window[1]]
