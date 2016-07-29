'''给一个整数数组，找到两个数使得他们的和等于一个给定的数target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是1到n，不是以0开头。

样例
numbers=[2, 7, 11, 15],  target=9

return [1, 2]

注意
你可以假设只有一组答案。'''
def twoSum(aList, n):
    
    for i in xrange(len(aList)):
        diff = n- aList[i]
        if diff in aList:
            return [i+ 1, aList.index(diff)+ 1]

print twoSum([2, 7, 11, 15], 23)    
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        length = len(numbers)
        tempdict = {}
        for i in xrange(length):
            tempdict[numbers[i]] = i
        for j in xrange(length):
            temp = target- numbers[j]
            if temp in tempdict.keys():
                return [j+ 1, tempdict[temp]+ 1]    
