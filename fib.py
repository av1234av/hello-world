def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


def fib2():
    a, b = 0, 1
    n = 2
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


def fib3(x):
    k = 0
    for i in fib2():
        if k < x:
            print(i)
            k += 1
        else:
            break


def fibonacci(n, first=0, second=1):
    while n != 0:
        yield first
        n, first, second = n-1, second, first+second


def fib4(n):
    assert n >=0
    list_results=[0,1]
    for i in range(2, n+1):
        list_results.append(list_results[i-1] + list_results[i-2])

    return list_results

if __name__ == '__main__':
    # print fib(10)
    print(fib(7))
    # print list(fibonacci(10))
