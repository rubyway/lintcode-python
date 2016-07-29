def bubbleSort(aList):
    #sort = False
    for i in xrange(len(aList), 0, -1):
        for j in xrange(1, i):
            if aList[j- 1] > aList[j]:
                aList[j- 1], aList[j] = aList[j], aList[j- 1]  #swap two elments
               #sort = False
    return aList
a = [1,4,3,7,2,9, 0]         
print bubbleSort(a) 
