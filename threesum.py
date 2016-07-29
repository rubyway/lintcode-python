'''给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

样例
如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

(-1, 0, 1)

(-1, -1, 2)

注意
在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。'''
def threeSum(aList):
    answers = []
    lenList = len(aList)
    if lenList < 3:
        return aList
    aList.sort()
    for i in xrange(lenList):
        target = -aList[i]
        if aList[i] > 0:
            break
        tempDict = {}
        for j in xrange(i+ 1, lenList):
            jvalue = aList[j]
            diff = target - jvalue
            if diff in tempDict:
                answer = (aList[i], diff, jvalue)
                if answer not in answers:
                    answers.append(answer)
            else:
                tempDict[jvalue] = j
    return answers
a = [-1, 0, 1, 2, -1, -4]
print threeSum(a)             
