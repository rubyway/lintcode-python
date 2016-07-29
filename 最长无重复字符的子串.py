#给定一个字符串，请找出其中无重复字符的最长子字符串。
"""样例
例如，在"abcabcbb"中，其无重复字符的最长子字符串是"abc"，其长度为 3。

对于，"bbbbb"，其无重复字符的最长子字符串为"b"，长度为1。

挑战 
O(n) 时间"""
#http://bookshadow.com/weblog/2015/04/05/leetcode-longest-substring-without-repeating-characters/
"""解题思路：
“滑动窗口法”

变量start和end分别记录子串的起点和终点

从左向右逐字符遍历原始字符串，每次将end + 1

字典countDict存储当前子串中各字符的个数

当新增字符c的计数 > 1时，向右移动起点start，并将s[start]在字典中的计数 - 1，直到countDict[c]不大于1为止

更新最大长度"""
def lengthOfLongestSubstring(s):
    length = len(s)
    if length == 0:
        return 0
    if length == 1:
        return 1
    start, end, xra = 0, 0, 0
    tempcount = {}
    
    for x in s:
        end += 1            
        tempcount[x] = tempcount.get(x, 0)+ 1
        while tempcount[x]> 1:
            tempcount[s[start]] -= 1 
            start += 1
        xra = max(xra, end- start)
    return xra
        
