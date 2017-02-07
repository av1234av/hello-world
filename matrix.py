import numpy

def transpose(m):
    t=[[0 for i in range(len(m))] for j in range(len(m[0]))]
    print t

    for i in range(len(m)):
        for j in range(len(m[0])):
            t[j][i] = m[i][j]
    return t

def matrixmult(m,n):
    rows_m = len(m)
    cols_m=len(m[0])
    rows_n=len(n)
    cols_n=len(n[0])

    result=[[0 for i in range(cols_n)] for j in range(rows_m)]

    for i in range(cols_n):
        for j in range(rows_m):
            for k in range(rows_n):
                result[i][j] += m[i][k]*n[k][j]
    return result

if __name__ == '__main__':
    matrix_a = [[1,2,3],
                [4,5,6]]
    matrix_b = [[1,2],
                [1,2],
                [1,2]]

    print transpose(matrix_a)
    print matrixmult(matrix_a, matrix_b)