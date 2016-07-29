def hailstone(n):
    tempList = []
    if n<= 1:
        return [1]#tempList.append(1)
    elif n%2 == 0:
        tempList.append(n)
        tempList.extend(hailstone(n/2))
    elif n%2 != 0:
        tempList.append(n)
        tempList.extend(hailstone(3*n+ 1))
    return tempList
a = 42
print hailstone(42)       
