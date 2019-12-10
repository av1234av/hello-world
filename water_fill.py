def water_fill(blocks, n):
    '''
    :param blocks:
    :param n:
    :return: total water filled

    '''
    left=[0]*n # max height to the left of the ith block
    right=[0]*n # max height to the right of the ith block

    left[0]=blocks[0]
    for i in range(1,n):     # go from left to right
        left[i]=max(left[i-1], blocks[i])

    right[n-1]=blocks[n-1]
    for j in range(n-2, -1, -1):   # go from right to left
        right[j]=max(right[j+1],blocks[j])

    water=0
    for k in range(0, n-1):
        water += min(left[k],right[k]) - blocks[k]

    return water
if __name__ == '__main__':
    print(water_fill([3,0,0,2,0,4],6))