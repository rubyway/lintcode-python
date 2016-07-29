"""


给出的n个非负整数表示每个直方图的高度，每个直方图的宽均为1，在直方图中找到最大的矩形面积。


以上直方图宽为1，高度为[2,1,5,6,2,3]。


最大矩形面积如图阴影部分所示，含有10单位
您在真实的面试中是否遇到过这个题？
样例

给出 height = [2,1,5,6,2,3]，返回 10

"""
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        length = len(height)
        if length == 0:
            return 0
        stack = []
        tempmax = 0
        height.append(0)
        i = 0
        while i<= length:
            if stack == [] or height[stack[-1]]<= height[i]:
                stack.append(i)
                i += 1
            else:
                temp = stack.pop()            
                tempmax = max(tempmax, height[temp]* (i if stack == [] else (i- stack[-1]- 1)))
        return tempmax
#http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
#http://www.cnblogs.com/mfryf/archive/2012/09/06/2672881.html
