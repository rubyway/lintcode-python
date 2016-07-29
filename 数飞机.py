'''给出飞机的起飞和降落时间的列表，用 interval 序列表示. 请计算出天上同时最多有多少架飞机？

样例
对于每架飞机的起降时间列表：[[1,10],[2,3],[5,8],[4,7]], 返回3。

注意
如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。'''
def covInput(aList):
    covList = []
    for i in aList:
        tempList = []        
        tempList = range(i[0],i[-1]+1)
        covList.append(tempList)
    return covList
    
def numPlane(aList):
    tempMax = 0
    tempList = []
    listmax = 0
    listmin = 0
    list4max = []
    list4min = []
    for i in aList:
        list4max.append(i[0])
        list4min.append(i[-1])
    listmax = max(list4max)
    listmin = min(list4min)
    tempMax = listmin
    tempList = covInput(aList)    
    for i in range(listmin, listmax+1):
        number = 0
        for j in tempList:
            if i != j[0] and i != j[-1] and i in j:
                number += 1
        if number >= tempMax:
            tempMax = number
    return tempMax
       
a = [[1,10],[2,3],[5,8],[4,7]]
#print covInput(a)
print numPlane(a)
