from typing import List

"""
DYNAMIC PROGRAMMING: matrix chain multiplication
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

    for diagonal in range(1, n):
        for i in range(0, n - diagonal):
            j = diagonal + i

            findBreakingPoint(m, s, p, i , j)

    return m, s

m, s = matrixChainMul([3, 5, 10, 2, 3])

for i in s:
    print(i)