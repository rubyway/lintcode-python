"""
乘积最大子序列
找出一个序列中乘积最大的连续子序列（至少包含一个数）。
样例
比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。"""
#动态规划：

#a>0时 最大值= max(最大正*a, a),更新最小负=最小负*a
#a<0时 最大值= 最小负*a，更新最小负 = min(最大正*a, a)
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        length = len(nums)
        temp = 0
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        posmax = [0]* length
        negmin = [0]* length
        posmax[0], negmin[0] = nums[0], nums[0]
    	for i in xrange(1, length):
    	    if nums[i] > 0:
                posmax[i] = max(posmax[i- 1]* nums[i], nums[i])
    	        negmin[i] = negmin[i- 1]* nums[i]
    	    if nums[i] < 0:
                negmin[i] = min(posmax[i- 1]* nums[i], nums[i])
                posmax[i] = negmin[i- 1]* nums[i]
            if posmax[i] > temp:
                temp = posmax[i]
        return temp
