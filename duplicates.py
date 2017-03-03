def remove_dupes(ll):
    i=0
    while i < len(ll):
        x=ll[i+1:].index(ll[i])
        if x:
            ll.remove(ll[x-1])
        # if ll[i] in ll[i+1:]:
        #     ll[i+1:].remove(ll[i])
        # else:
        i += 1

    return ll

def remove_dupes1(ll):
    for idx, item in enumerate(ll):
        if len(ll) <= idx: break
        if item in ll[:idx]:
            ll.pop(idx)

    return ll

if __name__ == '__main__':

    print remove_dupes([2,3,4,5,1,5,2,2,4,2,3])
    print remove_dupes1([2, 3, 4, 5, 1, 5, 2, 2, 4, 2, 3])