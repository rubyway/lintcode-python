def selectSort(aList):
    for i in xrange(len(aList)):
        minD = i
        for j in xrange(i+ 1, len(aList)):
            if aList[j] < aList[minD]:
                minD = j
        aList[i], aList[minD] = aList[minD], aList[i]
    return aList
a = [1,5,2,3,0,11,8]    
print selectSort(a)
