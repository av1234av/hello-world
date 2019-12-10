def two_sum(ll, summ):
    ll.sort()
    i = 0
    j = len(ll) - 1
    kount = 0
    while j > i:
        if ll[i] + ll[j] > summ:
            j -= 1
        if ll[i] + ll[j] < summ:
            i += 1
        else:
            idxI=i
            idxJ=j

            while j > i:
                if ll[i] != ll[idxI] and ll[j] != ll[idxJ]:
                    break
                if ll[i] == ll[idxI]:
                    i += 1
                if ll[j] == ll[idxJ]:
                    j -= 1

            for c in range(idxI, i):
                for b in range(idxJ, j, -1):
                    print('{0} + {1}'.format(ll[c],ll[b]))
                    kount += 1
    print(kount)

if __name__ == '__main__':
    two_sum([5,2,6,8,15,3,1,7,5],13)