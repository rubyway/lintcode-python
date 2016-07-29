def happyNum(n):
    tempList = []
    if n == 1:
        return True
    tempn = n
    while True:
        temp = 0
        for i in str(tempn):
            temp += (int(i))**2
        if temp == 1:
            return True
        elif temp in tempList:
            return False
        tempList.append(temp)
        tempn = temp
print happyNum(19) 
