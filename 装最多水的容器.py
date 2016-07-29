#http://www.lintcode.com/zh-cn/problem/container-with-most-water/
"""给定 n 个非负整数 a1, a2, ..., an, 每个数代表了坐标中的一个点 (i, ai)。画 n 条垂直线，使得 i 垂直线的两个端点分别为(i, ai)和(i, 0)。找到两条线，使得其与 x 轴共同构成一个容器，以容纳最多水。

 注意事项

容器不可倾斜。

给出[1,3,2], 最大的储水面积是2."""
"""
http://blog.csdn.net/lanyu317/article/details/22693685
有两个指针i和j分别指向头和尾， 如果a[i]<a[j], 则i++,否则j--:

证明：

对任意ｋ<j：

都有(k-i)*min(a[k],a[i]) < (j-i)min(a[j],a[i]) = (j-i)a[i]

因为：

(k-i) < (j-i)

min(a[k],a[i]) < a[i] < min(a[j],a[i])

所以此种情况移动j只能得到更小的值， 移动j无用， 只能移动i。 反之亦然。"""
def maxArea(self, heights):
    length = len(heights)
    if length == 0 or length == 1:
        return 0
    if length == 2:
        return min(heights)
    left, right, temparea =0, length-1, 0
    while left< right:
        area = min(heights[left], heights[right])* (right- left)
        temparea = area if area>= temparea else temparea
        if heights[left]< heights[right]:
            left += 1
        else:
            right -= 1
    return temparea
         




