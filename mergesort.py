def mergesort(ll):
    if len(ll) > 1:
        mid = len(ll) // 2
        left=ll[mid:]
        right=ll[:mid]
        mergesort(left)
        mergesort(right)
        ll=_merge(ll,left=left,right=right)
        return ll

def _merge(ll,left,right):
    i=j=k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ll[k] = left[i]
            i += 1
        else:
            ll[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        ll[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        ll[k] = right[j]
        k += 1
        j += 1

    print 'left:{0} right:{1}'.format(left, right)
    return ll

if __name__ == '__main__':

    print(mergesort([4,7,1,8,33,25,91,95,54]))