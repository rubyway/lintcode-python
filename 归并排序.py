def mergeSort(aList):
    if len(aList)<= 1:
	return aList
    mid= len(aList)/ 2
    left= mergeSort(aList[:mid])
    right= mergeSort(aList[mid:])
    return merge(left,right)

def merge(left,right):
    result= []
    i,j= 0,0
    while i< len(left) and j< len(right):
        if left[i]<= right[j]:
            result.append(left[i])
	    i+= 1
	else:
	   result.append(right[j])
           j+= 1
    result+= left[i:]
    result+= right[j:]
    return result

if __name__=='__main__':
	a = [2, 7, 1, 9, -7, 12, 100, 4, 7, 0, 11, -2, 3]
	print mergeSort(a)
	
