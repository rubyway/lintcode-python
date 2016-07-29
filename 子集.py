"""


给定一个含不同整数的集合，返回其所有的子集
注意事项

子集中的元素排列必须是非降序的，解集必须不包含重复的子集
您在真实的面试中是否遇到过这个题？
样例

如果 S = [1,2,3]，有如下的解：

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        length = len(S)
        result, temp = [], []
        if length == 0:
            return []
        S.sort()
        self.search(result, temp, S)
        return result
        
    def search(self, result, temp, S):
        result.append(temp)
        length = len(S)
        for i in xrange(length):
            self.search(result, temp+ [S[i]], S[i+1:])
        
