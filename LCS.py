#http://blog.csdn.net/littlethunder/article/details/25637173
def LCSLength(m, n, x=None, y=None,c=None, b=None):
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 'equals'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'up'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'left'
 
def GetLCS(i, j, x=None, b=None):
    if i == 0 and j == 0:
        return
    if b[i][j] == 'equals':
        GetLCS(i-1,j-1, x, b)
        print x[i-1], ' '
    elif b[i][j] == 'left':
        GetLCS(i, j-1, x, b)
    else:
        GetLCS(i-1, j, x, b)
 
 
if __name__ == '__main__':
    x ="ABCBDAB"
    y = "BDCABA"
    m = len(x)+1
    n = len(y)+1
    b = [[0 for i in range(n)] for j in range(m)]
    c = [[0 for i in range(n)] for j in range(m)]
 
    LCSLength(m,n,x,y,c,b)
    #for i in c:
     #   print i
    #for j in b:
     #   print j
    GetLCS(m-1,n-1,x,b)
