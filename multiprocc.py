from multiprocessing import Process, Pool, Array, Manager
from concurrent import futures
import math


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for p in range(3,sqrt_n+1, 2):
        if n % p == 0:
            return False
    return True


def f(n):
    sum = 0
    for i in range(1000):
        sum += n * n

    return sum

def multiprocess_with_futures():
    with futures.ProcessPoolExecutor(2) as executor:
        e=executor.map(f,range(100))
    for x in e:
        print x
def multiprocess_using_Pool():
    p = Pool()
    p.map(f,range(10000))
    p.close()
    p.join()

def fn(n, result_set):
    for idx, x in enumerate(n):
        result_set[idx] = x * x

def process_using_shared():
    n=[1,2,3,4]
    result_set=Array('i',4)
    p = Process(target=fn,args=(n,result_set))
    p.start()
    p.join()

    print (result_set[:])

if __name__ == '__main__':
    PRIMES = [5,
              112272535095293,
              112582705942171,
              112272535095293,
              115280095190773,
              115797848077099,
              1099726899285419]

    from time import time
    t1=time()
    multiprocess_using_Pool()
    print 'processing times {}'.format(time()-t1)

    t2=time()
    for x  in range(10000):
        f(x)

    print 'single proc times {}'.format(time()-t2)

    process_using_shared()
    m = Manager()
    d = m.dict
    l=m.list

    multiprocess_with_futures()

    t1=time()
    for number, prime in zip(PRIMES,map(is_prime, PRIMES)):
        print '%d is %s' % (number,prime)
    print 'took {} secs'.format(time()-t1)

    t1 = time()
    with futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print '%d is %s' % (number,prime)
    print 'took {} secs with concurrent.futures'.format(time()-t1)