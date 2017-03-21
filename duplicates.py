def remove_dupes(ll):
    i=0
    while i < len(ll):
        x=ll[i+1:].index(ll[i])
        if x:
            ll.remove(ll[x+1])
        # if ll[i] in ll[i+1:]:
        #     ll[i+1:].remove(ll[i])
        # else:
        i += 1

    return ll

def remove_dupes1(ll):
    new_ll=[]
    for i in range(len(ll)):
        if ll[i] in ll[i+1:]:
            continue
        new_ll.append(ll[i])
    return new_ll

if __name__ == '__main__':

    # print remove_dupes([2,3,4,5,1,5,2,2,4,2,3])
    ll=[2, 3, 4, 5, 1, 5, 2, 2, 4, 2, 3]

    print [ll[i] for i in range(len(ll)) if ll[i] not in ll[i+1:]]
    print remove_dupes1(ll)