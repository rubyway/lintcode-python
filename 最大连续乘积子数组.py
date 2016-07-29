def maxlist(aList):
    maxMul = aList[0]
    for i in xrange(len(aList)):
        temp = 1
        for j in xrange(i, len(aList)):
            temp *= aList[j]
            if temp > maxMul:
                maxMul = temp
    return maxMul
        
a = [-2.5, 4, 0, 3, 0.5, 8, -1] 
print maxlist(a)           

def newMaxMul(aList):
    maxend = aList[0]
    minend = aList[0]
    maxResult = aList[0]
    for i in xrange(1, len(aList)):
        end1 = maxend* a[i]
        end2 = minend* a[i]
        maxend = max(max(end1, end2), a[i])
        minend = min(min(end1, end2), a[i])
        maxResult = max(maxResult, maxend)
    return maxResult
a = [-2.5, 4, 0, 3, 0.5, 8, -1] 
print newMaxMul(a)          
        
