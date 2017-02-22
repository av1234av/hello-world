def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


def fib2():
    a,b=0,1
    n=2
    yield a
    yield b
    while True:
        a,b=b,a+b
        yield b

def fib3(x):
    kount=0
    for i in fib2():
        if kount < x:
            print i
            kount += 1
        else:
            break

def fibonacci(n, first=0, second=1):
    while n != 0:
        yield first
        n,first,second = n-1, second, first+second

if __name__ == '__main__':
    # print fib(10)
    fib3(10)
    print list(fibonacci(10))
