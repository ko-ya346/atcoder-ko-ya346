def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

n, w = map(int, input().split())

d = [[float("inf")]*n for _ in range(n)]

for i in range(w):
    x,y,z = map(int, input().split())
    d[x][y] = z
    d[y][x] = z
# print(d)

for j in range(n):
    d[j][j] = 0
print(warshall_floyd(d))

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

csr = csr_matrix(d)
print(floyd_warshall(csr) == np.array(warshall_floyd(d)))

'''
入力例
7 10
0 1 2
0 2 5
1 2 4
2 3 2
1 3 6
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9
'''