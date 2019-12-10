# Given two sorted arrays A and B merge them into A (it has enough space to hold B)
# keeping them sorted.

def merge_two_sorted_arrays(A, B):
    ''' Use the merge from end of the array'''
    i = len(A)
    last_b = len(B)-1
    last_a = (i - len(B))-1

    while last_a >= 0 and last_b >= 0:
        if A[last_a] > B[last_b]:
            A[i-1] = A[last_a]
            last_a-=1
        else:
            A[i-1] = B[last_b]
            last_b-=1
        i-=1

    # while last_a >= 0:
    #     A[i-1] = A[last_a]
    #     last_a-=1
    #     i-=1

    while last_b >= 0:
        A[i-1] = B[last_b]
        last_b-=1
        i-=1

    return A

if __name__ == '__main__':
    A = [3,4,5,7,8,21,37,None,None,None,None,None,None,None]
    B = [1,2,9,10,16,18,26]
    print(merge_two_sorted_arrays(A, B))