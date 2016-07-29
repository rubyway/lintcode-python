def findLessThanValue(L, Value):
    #L in order
    # find the index which value is the Maximum of all the value less than given Value
    length = len(L)
    if length == 0:
        return False
    if Value > L[-1]:
        return L[-1]
    elif Value < L[0]:
        return False
    else:
        if Value in L:
            return L[L.index(Value)- 1]
        left = 0
        right = length- 1
        while(left <= right):
            mid = left + ((right- left) >> 1)
            print left, mid, right
            if(L[mid] > Value):
                right = mid
            elif (L[mid] < Value):
                left = mid
            if (right- left) == 1:
                return L[left]
a = [1, 2, 3, 4, 5,7, 7,8, 9, 13, 50]           
print findLessThanValue(a, 6) 
        
    
    
    
    
