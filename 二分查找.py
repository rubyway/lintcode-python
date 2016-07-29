def bifind(aList, value):
    left = 0
    right = len(aList)- 1
    if value < aList[left] or value > aList[right]:
        return False
    while(left < right):
        mid = left + ((right- left) >> 1)
        print left, mid, right
        if(aList[mid] > value):
            right = mid
        elif (aList[mid] < value):
            left = mid
        else:
            return mid, aList[mid]
    return False
a = range(1, 10)            
print bifind(a, 0)   
