def editDis(sList, tList):
    tempList = [[0 for col in range(len(tList)+ 1)] for row in range(len(sList)+ 1)]
    for i in xrange(len(sList)+ 1):
        tempList[i][0] = i
    for j in xrange(len(tList)+ 1):
        tempList[0][j] = j
    for m in xrange(1, len(sList)+ 1):
        for n in xrange(1, len(tList)+ 1):
            d, temp = 0, 0            
            temp = min(tempList[m- 1][n], tempList[m][n- 1])+ 1
            if sList[m- 1] == tList[n- 1]:
                d = 0
            else:
                d = 1
            tempList[m][n] = min(temp, tempList[m- 1][n- 1]+ d)
    print tempList
    return tempList[len(sList)][len(tList)]
print editDis("aaaaabaaaaa", "aaaaacaabaa")    
    
#July《编程之法：面试和算法心得》第5.2节
    
