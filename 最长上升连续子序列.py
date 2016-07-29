# -*- coding: utf-8 -*-
def convertf(A):
    tempList = []
    lenA = len(A)
    for i in xrange(1, lenA):
        if A[i] > A[i- 1]:
            tempList.append(1)
        elif A[i] < A[i- 1]:
            tempList.append(-1)
        elif A[i] == A[i- 1]:
            tempList.append(0)
    return tempList
    
def repeatTimes(tempList):
    '''
    [0, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1]
    {1: 1, 2: 4, 3: 4, 4: 3}
    
    
    '''
    temp = 0#当相邻元素不同时计数加1
    count = 1#相同元素计数
    Allcount = 0#结尾相同元素之前的所有元素个数
    lenTempList = len(tempList)
    tempCount = {}
    for j in xrange(1, lenTempList):

        if tempList[j- 1] != tempList[j]:
            temp += 1
            tempCount[temp] = count
            Allcount += count
            count = 1
        elif tempList[j- 1] == tempList[j]:
            count += 1
    tempCount[temp+ 1] = lenTempList - Allcount
    return tempCount
def longestIncreasingContinuousSubsequence(aList):
    tempDict = repeatTimes(convertf(aList))
    (a, b) = max(tempDict.items(), key=lambda x: x[1])
    #return max(tempDict.items(), key=lambda x: x[1])
    count = 0
    for i in xrange(1, a):
        count += tempDict[i]
    return aList[count: count+ b+ 1]
        
    
    
                   
a = [5,5,4,3,2,0, 1, 2, 3, 4,8,5,4, 3, 2, 1]
print a
print convertf(a)
print repeatTimes(convertf(a))
print longestIncreasingContinuousSubsequence(a)
