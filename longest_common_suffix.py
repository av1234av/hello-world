def lcsuffix(str1, str2):
    lst1 = list(str1)
    lst2 = list(str2)

    x=lst1.pop()
    y=lst2.pop()

    out = []

    while (x == y):
        out.append(x)
        if lst1 and lst2:
            x = lst1.pop()
            y = lst2.pop()
        else:
            break

    print ''.join(reversed(out))

def longest_common_suffix(str1, str2):
    lst=zip(str1[::-1],str2[::-1])
    out=[]
    for x in lst:
        if x[0] == x[1]:
            out.append(x[0])
        else:
            break
    print ''.join(out[::-1])

    # out=[x[0] for x in lst if x==(x[0],)*len(x)][::-1]
    # print ''.join(out)

if __name__ == '__main__':
    lcsuffix('Cornfield','rtfield')
    longest_common_suffix('Cornfield','rtfield')