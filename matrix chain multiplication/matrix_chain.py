from typing import List

"""
TODO:
Clean and explain the code

DYNAMIC PROGRAMMING: matrix chain multiplication

Example: A1 A2 A3 A4 A5
"""

def findBreakingPoint(m, s, p, i, j):
    m[i][j] = None

    for k in range(i, j):
        q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1] 
    
        if m[i][j] is None or q < m[i][j]:
            m[i][j] = q
            s[i][j] = k

def matrixChainMul(p: List[int]):
    n = len(p) - 1
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    """
    We can compute m diagonal by diagonal starting from the main
    diagonal.
    We don't need to do anything for the main diagonal. It is just 0.
    """

    # n is the number of matrix that we want to multiply
    for diagonal in range(1, n):
        for i in range(0, n - diagonal):
            j = diagonal + i

            findBreakingPoint(m, s, p, i , j)

    return m, s

m, s = matrixChainMul([3, 5, 10, 2, 3])

for i in s:
    print(i)