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

if __name__ == '__main__':
    # print fib(10)
    fib3(10)
