"""


给出一组候选数字(C)和目标数字(T),找到C中所有的组合，使找出的数字和为T。C中的数字可以无限制重复被选取。

例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：

[7]，

[2,2,3]
注意事项

    所有的数字(包括目标数字)均为正整数。
    元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
    解集不能包含重复的组合。 

您在真实的面试中是否遇到过这个题？
样例

给出候选数组[2,3,6,7]和目标数字7

返回 [[7],[2,2,3]]
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        result, temp = [], []
        self.search(candidates, target, temp, result)
        return result

    def search(self, candidates, target, temp, result):
        length = len(candidates)
        if length == 0 or sum(temp) > target:
            return
        if sum(temp) == target:
            result.append(temp)
            return    
        for i in xrange(length):
            self.search(candidates[i:], target, temp+ [candidates[i]], result)

        
