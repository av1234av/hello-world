def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a % b)

def lcm(a, b):
    return (a/gcd(a,b))*b

if __name__ == '__main__':
    print gcd(180,120)
    print lcm(180,120)