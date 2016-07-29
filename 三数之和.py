"""


给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。
注意事项

在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。
您在真实的面试中是否遇到过这个题？
样例

如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

(-1, 0, 1)

(-1, -1, 2)
"""
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):

    #print twosum([-2, -1, 0, 1, 2, 3], 0)
        length = len(numbers)
        numbers = sorted(numbers)
        result = []
        for i in xrange(length-1):
            #remain = target- numbers[i]
            remain = 0- numbers[i]
            scan = numbers[i]
            temp = numbers[0:i]+numbers[i+1::]     
            addtwo = self.twosum(temp, remain)
            if addtwo == []:
                continue
            else:
                for j in addtwo:
                    templist = []
                    templist.append(scan)
                    templist.extend(j)
                    templist = sorted(templist)
                    if templist not in result:
                        result.append(templist)
        ans = []
        for k in result:
            ans.append(tuple(k))
        return ans
        
    def twosum(self,alist, target):
        length = len(alist)
        i,j = 0, length-1
        #alist = sorted(alist)
        result = []
        while i<j:
            temp = alist[i] + alist[j]
            if temp == target:
                result.append([alist[i],alist[j]])
                i += 1
                j -= 1
            elif temp < target:
                i += 1
            else:
                j -= 1
        return result
