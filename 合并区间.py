'''给出若干闭合区间，合并所有重叠的部分。

样例
给出的区间列表 => 合并后的区间列表：

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
挑战
O(n log n) 的时间和 O(1) 的额外空间。'''
def mergerinter(aList):
    aList.sort(key = lambda x: x[0])
    #return aList
    length = len(aList)
    tempList = []
    if length == 0:
        return tempList
    tempList.append(aList[0])
    for i in xrange(1, length):
        newlength = len(tempList)
        if aList[i][0] in range(tempList[newlength-1][0], tempList[newlength-1][1]+ 1):
            tempList[newlength- 1][1] = max(aList[i][1], tempList[newlength-1][1])
        else:
            tempList.append(aList[i])
    return tempList
a = [[1,3],[2,9],[8,29],[15,18]]
print mergerinter(a)
