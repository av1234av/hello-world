def qsort(l):
    qsorthelper(l,0,len(l)-1)
    print l

def qsorthelper(l, first, last):
    if first < last:
        pivot = partition(l,first,last)
        qsorthelper(l,first,pivot-1)
        qsorthelper(l,pivot+1,last)

def partition(l,first,last):
    leftmark = first + 1
    rightmark = last

    while True:

        while leftmark <= rightmark and l[leftmark] <= l[first]:
            leftmark += 1
        while leftmark <= rightmark and l[rightmark] >= l[first]:
            rightmark -= 1

        if leftmark < rightmark:
            temp = l[leftmark]
            l[leftmark] = l[rightmark]
            l[rightmark] = temp
        else:
            break

    print l

    pivot = l[first]
    l[first]=l[rightmark]
    l[rightmark]=pivot

    return rightmark

if __name__ == '__main__':
    qsort([3,4,2,88,42,77,39,18,56])