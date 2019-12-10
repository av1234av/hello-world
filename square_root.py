def square_root(n):
    min = 1
    max = n
    mid = 1
    while mid >= min:
        mid = (min + max)/2
        guess = mid * mid
        if abs(guess - n) <= 0.0001:
            return mid
        elif guess > n:
            max = mid
        else:
            min = mid


# Recursive implementation
def square_root_1(n):
    return square_root_rec(n,1,n)


def square_root_rec(n, min, max):
    mid = (min + max)/2
    guess = mid * mid
    if abs(guess - n) <= 0.0001:
        return mid
    elif guess > n:
        return square_root_rec(n,min,mid)
    else:
        return square_root_rec(n,mid,max)

if __name__ == "__main__":
    print(square_root(3))
    print(square_root_1(3))