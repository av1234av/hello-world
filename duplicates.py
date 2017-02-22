def remove_dupes(ll):
    i=0
    while i < len(ll):
        if ll[i] in ll[i+1:]:
            ll.remove(ll[i])
        else:
            i += 1

    return ll

def remove_dupes1(ll):
    for idx, item in enumerate(ll):
        if len(ll) <= idx: break
        if item in ll[:idx]:
            ll.pop(idx)

    return ll

def gen():
    for i in range(20):
        yield i
        if i == 15:
            return


if __name__ == '__main__':
    # print remove_dupes([2,3,4,5,1,5,2,2,4,2,3])
    # print remove_dupes1([2, 3, 4, 5, 1, 5, 2, 2, 4, 2, 3])
    try:
        l=[x for x in gen()]
    except Exception as e:
        print e

    print l