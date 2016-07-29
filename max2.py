def findmax2(aList):
    a = max(aList)
    aList.remove(a)
    b = max(aList)
    return (a, b)
a = [0, 1, 2, 3, 4, 7, 9]
print findmax2(a)    



def findmax2_new1(aList):
    max1, max2 = aList[0], aList[1]
    if max1 < max2:
        max1, max2 = max2, max1
    for i in xrange(2, len(aList)):
        if max2 < aList[i]:
            max2 = aList[i]
            if max1 < max2:
                max1, max2 = max2, max1
    print (max1, max2)
a = [0, 1, 2, 3, 4, 7, 9]
print findmax2_new1(a)                  

#d-c 5n/3+2
