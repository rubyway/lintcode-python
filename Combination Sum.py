"""
题目描述：
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]
Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]"""
def conbinationsum(k, target):
    result = []
    def search(start, count, sigma, nums):
        if count > k or sigma > target:
            return
        if count == k and sigma == target:
            result.append(nums)
            return
        for i in xrange(start+ 1, 10):
            search(i, count+ 1, sigma+ i, nums+ [i])
    search(0, 0, 0, [])
    return result
a = 4
b = 19
print conbinationsum(a, b)
