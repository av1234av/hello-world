def matrixBlockSum(mat, k):
    rows, cols = len(mat), len(mat[0])
    prefixSum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    # Calculate prefix sum
    for i in range(rows): # O(n*m)
        for j in range(cols):
            prefixSum[i+1][j+1] = mat[i][j] + prefixSum[i][j+1] + prefixSum[i+1][j] - prefixSum[i][j]

    answer = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows): # O(n*m)
        for j in range(cols):
            r1 = max(0, i-k)
            c1 = max(0, j-k)
            r2 = min(rows - 1, i+k)
            c2 = min(cols -1, j+k)

            answer[i][j] = prefixSum[r2+1][c2+1] - prefixSum[r1][c2+1] - prefixSum[r2+1][c1] + prefixSum[r1][c1]

    return answer
if __name__ == '__main__': 
   matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
   print(matrixBlockSum(matrix_a, 1))