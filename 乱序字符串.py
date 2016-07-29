'''给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

样例
对于字符串数组 ["lint","intl","inlt","code"]

返回 ["lint","inlt","intl"]

注意
所有的字符串都只包含小写字母'''
def anagrams(c):
    newtemp = [[]]*len(c)
    for k in xrange(len(c)):
        newtemp[k] = sorted(c[k])
    temp = []
    for l in newtemp:
        atemp = ''
        for n in l:
             atemp += n
        temp.append(atemp)
    tempdict = {}
    d = set(temp)
    e = [m for m in d]
    for i in e:
        aa = []
        for j in xrange(len(temp)): 
            if i == temp[j]:
                aa.append(j)
        tempdict[i] = aa
    return tempdict
def helper(c):
    temp = anagrams(c)
    lasttemp = []
    for i in temp:
        #newtemp = []
        if len(temp[i]) >1:
            newtemp = []
            for j in temp[i]:
                newtemp.append(c[j])
            lasttemp.append(newtemp)
    return lasttemp
           
            
c = ['abc', 'cba', 'dcb', 'def', 'cab', 'bcd']  
print helper(c) 
