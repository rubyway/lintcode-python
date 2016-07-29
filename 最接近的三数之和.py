"""


给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。
注意事项

只需要返回三元组之和，无需返回三元组本身
您在真实的面试中是否遇到过这个题？
样例

例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
    #def threeSumClosest(numbers, target):
        length = len(numbers)
        numbers = sorted(numbers)
        mindiff = 2^32
        result = 0
        for i in xrange(length- 2):
            j = i+ 1
            k = length- 1
            while j < k:
                sums = numbers[i] + numbers[j] + numbers[k]
                if sums == target:
                    return sums
                diff = abs(sums- target)
                
                if diff < mindiff:
                    mindiff = diff
                    result = sums
                if sums > target:
                    k -= 1
                elif sums < target:
                    j += 1
        return result
