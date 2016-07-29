#蛮力求解
def countDigitOnes(n):
    count = 0
    for i in xrange(1, n+ 1):
        for j in str(i):
            if j == '1':
                count += 1
    return count
print countDigitOne(13)    
#观察每一位1的个数
#http://www.cnblogs.com/aniy/articles/4676538.html
def countDigitOnes(n):
    count, i = 0, 1
    while i <= n:
        a, b = n/ i, n% i
        count += (a+ 8)/10 * i + int(a% 10== 1)*(b+ 1)
        i *= 10
    return count
print countDigitOnes(13)
