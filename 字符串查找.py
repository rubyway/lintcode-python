"""
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

说明
在面试中我是否需要实现KMP算法？

不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。
样例
如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。"""
class Solution:
    def strStr(self, source, target):
        if source is None and target != "":
            return -1
        if source and target is None:
            return -1
        lengths, lengtht = len(source), len(target)
        i = 0
        if source == " " and target == " ":
            return 0

        if target not in source:
            return -1
        while i < lengths- lengtht + 1:
            if source[i: i+ lengtht] == target:
                return i
            i += 1
        
