import math


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for p in range(3,sqrt_n+1, 2):
        if n % p == 0:
            return False
    return True


def primes(n):
    array=[0,1,2]
    array += [x if x%2 else False for x in range(3,n)]
    for p in range(3,int(math.sqrt(n)),2):
        if array[p]:
            # remove multiples of p
            for m in range(p*p, n, 2*p):
                array[m] = False
    return [p for p in array if p > 1]

if __name__ == '__main__':
    print primes(100)