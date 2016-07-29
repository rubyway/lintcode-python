"""


给出一组候选数字(C)和目标数字(T),找出C中所有的组合，使组合中数字的和为T。C中每个数字在每个组合中只能使用一次。
注意事项

    所有的数字(包括目标数字)均为正整数。
    元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
    解集不能包含重复的组合。 

您在真实的面试中是否遇到过这个题？
样例

给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,

解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]
"""
class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        candidates.sort()
        result, temp = [], []
        self.search(candidates, target, temp, result)
        return result

    def search(self, candidates, target, temp, result):
        length = len(candidates)
        if sum(temp) > target:
            return
        if sum(temp) == target:
            if temp not in result:
                result.append(temp)
                return
        i = 0
        while i< length:
            self.search(candidates[i+ 1:], target, temp+ [candidates[i]], result)
            while (i+ 1)< length and candidates[i] == candidates[i+ 1]:
                i += 1
            i += 1
