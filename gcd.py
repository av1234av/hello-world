# import fire
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a % b)

def lcm(a, b):
    return (a/gcd(a,b))*b

if __name__ == '__main__':
    # fire.Fire(gcd)
    # fire.Fire(lcm)
    print(gcd(300,1200))