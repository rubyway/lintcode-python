def insertSort(aList):
    for i in range(1,len(aList)):  
        while i> 0 and aList[i] < aList[i- 1]:
            aList[i], aList[i- 1] = aList[i- 1], aList[i]
            i-= 1
    return aList  
 
a = [5,7,2,9,1]  
print insertSort(a) 
