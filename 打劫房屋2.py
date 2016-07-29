"""
在上次打劫完一条街道之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子围成了一个圈，这就意味着第一间房子和最后一间房子是挨着的。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

 注意事项

这题是House Robber的扩展，只不过是由直线变成了圈

您在真实的面试中是否遇到过这个题？ Yes
样例
给出nums = [3,6,4], 返回　6，　你不能打劫3和4所在的房间，因为它们围成一个圈，是相邻的．"""
class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))#打劫第一个和打劫最后一个取得的最大值
    def helper(self, nums):
        length = len(nums)
        odd, even = 0, 0
        for i in xrange(length):
            if i% 2:
                odd = max(odd+ nums[i], even)#奇数位打劫或者不打劫能得到的最大值
            else:
                even = max(even+ nums[i], odd)#偶数位打劫或者不打劫能得到的最大值
        return max(odd, even)
