import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """

    n = len(A)
    m = len(A[0])
    matrix = np.zeros((m,n))

    for i in range(0, n):
        for j in range(0, m):
            matrix[j][i] = A[i][j]

    
    return matrix
