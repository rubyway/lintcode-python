def fib(n):
    return n if 2 > n else fib(n- 1) + fib(n- 2)  
print fib(6)

def fib_new1(n):
    f, g = 0, 1
    while(0<n- 1):
        g = f + g
        f = g - f
        n -= 1
    return g
print fib_new1(6)
