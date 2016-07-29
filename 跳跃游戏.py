"""
跳跃游戏

给出一个非负整数数组，你最初定位在数组的第一个位置。　　　

数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　

判断你是否能到达数组的最后一个位置。


这个问题有两个方法，一个是贪心和 动态规划。


样例
A = [2,3,1,1,4]，返回 true.

A = [3,2,1,0,4]，返回 false."""
#https://leetcode.com/discuss/55483/java-answer-for-jump-game?show=55483#q55483
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        length = len(A)
        maxjump = 0
        for i in xrange(length):
            if i > maxjump:
                return False
            maxjump = max(maxjump, A[i]+ i)
        return True
