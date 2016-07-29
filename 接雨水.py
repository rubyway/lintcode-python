#给出 n 个非负整数，代表一张X轴上每个区域宽度为 1 的海拔图, 计算这个海拔图最多能接住多少（面积）雨水。
#海拔分别为 [0,1,0,2,1,0,1,3,2,1,2,1], 返回 6.
def trapRainWater(heights):
    length = len(heights)
    i = 0
    j = 1
    sumdrop = 0
    while i< length- 1 and j< length: 
        if heights[j] >= heights[i]:
            for k in xrange(i+ 1, j):
                if heights[k] <= min(heights[i], heights[j]):
                    sumdrop += (min(heights[i], heights[j])- heights[k])
            i = j
            j += 2
        else:
            j += 1
            if heights[i] > max(heights[i+ 1:length]):
                i += 1 
    return sumdrop
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print trapRainWater(a)
