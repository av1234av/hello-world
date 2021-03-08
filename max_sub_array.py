# Largest sum contiguous subarray
def max_subarray(a):
    max_now=a[0]
    max_so_far=a[0]
    for i in range(1, len(a)):
        max_now=max(a[i], max_now+a[i])
        max_so_far=max(max_so_far, max_now)
    return max_so_far

if __name__ == '__main__':
    a=[1,4,-5,7,-3,24]
#    a=[-2,-3,4,-1,-2,1,5,-3]
    print(a)
    print(max_subarray(a))