from multiprocessing import Process, Pool, Array, Manager


def f(n):
    sum = 0
    for i in range(1000):
        sum += n * n

    return sum


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
