def findHalf(aList):
    #tempList = aList[:]
    length = len(aList)- 1
    candi = aList[0]
    nTimes = 1
    #i = 0
    #while i < length:
    for i in range(length):
        if nTimes == 0:
            candi = aList[i]
            nTimes = 1        
        else:
            if aList[i+ 1] == candi:
                nTimes += 1
            else:
                nTimes -= 1
    return candi


a = [3,5,5, 4,5,5, 5,5,5,5,56,5,4,5, 5,2,5,8, 5, 9, 9]    
print findHalf(a) 
