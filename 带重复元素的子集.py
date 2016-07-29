"""


给定一个可能具有重复数字的列表，返回其所有可能的子集
注意事项

    子集中的每个元素都是非降序的
    两个子集间的顺序是无关紧要的
    解集中不能包含重复子集

您在真实的面试中是否遇到过这个题？
样例

如果 S = [1,2,2]，一个可能的答案为：

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        length = len(S)
        result, temp = [], []
        if length == 0:
            return []
        S.sort()
        self.search(result, temp, S)
        return result
        
    def search(self, result, temp, S):
        if temp not in result:
            result.append(temp)
        length = len(S)
        for i in xrange(length):
            self.search(result, temp+ [S[i]], S[i+1:])
#高效的方法
#https://github.com/algorhythms/LeetCode/blob/master/090%20Subsets%20II.py        
