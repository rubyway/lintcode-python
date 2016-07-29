"""


给定一个整数数组来表示排列，找出其之后的一个排列。
注意事项

排列中可能包含重复的整数
您在真实的面试中是否遇到过这个题？
样例

给出排列[1,3,2,3]，其下一个排列是[1,3,3,2]

给出排列[4,3,2,1]，其下一个排列是[1,2,3,4]
"""
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
    #def nextPermutation(num):
        length = len(num)
        if length <= 1:
            return num
        i = 1
        while i< length:
            if num[i-1] >= num[i]:
                if i == (length-1):
                    return num[::-1]
                i += 1
            else:
                break
            
        for i in xrange(length-1, 0, -1):
            if num[i- 1] < num[i]:
                #swap1 = num[i-1]
                for j in xrange(length-1, i-1, -1):
                    if num[j] > num[i- 1]:
                        num[j], num[i-1] = num[i-1], num[j]
                        break
                return num[:i]+ num[i:][::-1]
