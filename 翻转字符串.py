"""
给定一个字符串，逐个翻转字符串中的每个单词。


说明
单词的构成：无空格字母构成一个单词
输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
样例
给出s = "the sky is blue"，返回"blue is sky the"""
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        length = len(s)
        if s == "":
            return ''
        if s == ' '*length:
            return ''
        templist = []
        tempstr = ''
        for i in s:
            if i == ' ':
                templist.append(tempstr)
                tempstr = ''
            if i != ' ':
                tempstr += i
        templist.append(tempstr)
        temp = ''
        lengtht = len(templist)
        for j in xrange(lengtht- 1, -1, -1):
            temp += templist[j]
            temp += ' '           
        temp = temp[:-1]
        lengthtemp = len(temp)
        for i in xrange(lengthtemp):
            if temp[i] != ' ':
                return temp[i:]
