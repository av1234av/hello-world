import numpy

def transpose(m):
    t=[[0 for i in range(len(m))] for j in range(len(m[0]))]
    print(t)

    for i in range(len(m)):
        for j in range(len(m[0])):
            t[j][i] = m[i][j]
    return t

def matrixmult1(m,n):
    n_zip=zip(*n)
    result=[]
    for row_m in m:
        ll=[]
        for col_n in n_zip:
            sum = 0
            for a,b in zip(row_m, col_n):
                sum +=a * b
            ll.append(sum)
        result.append(ll)
    return result

def matrixmult2(m,n):
    n_zip=zip(*n)
    result = [[sum(a * b for a,b in zip(row_m, col_n)) for col_n in n_zip] for row_m in m]
    print result

def matrixmult(m,n):
    rows_m = len(m)
    cols_m=len(m[0])
    rows_n=len(n)
    cols_n=len(n[0])

    result=[[0 for i in range(cols_n)] for j in range(rows_m)]

    for i in range(rows_m):
        for j in range(cols_n):
            for k in range(rows_n):
                result[i][j] += m[i][k]*n[k][j]
    return result

if __name__ == '__main__':
    matrix_a = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    matrix_b = [[1,2],
                [1,2],
                [1,2]]

    print 'transpose {}'.format(transpose(matrix_a))
    print 'result from matmul {}'.format(matrixmult(matrix_a, matrix_b))
    print 'result from matrixmult1 {}'.format(matrixmult1(matrix_a, matrix_b))
    print matrixmult2(matrix_a, matrix_b)