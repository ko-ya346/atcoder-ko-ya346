# def warshall_floyd(d):
#     #d[i][j]: iからjへの最短距離
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 d[i][j] = min(d[i][j], d[i][k] + d[k][j])
#     return d

# n, w = map(int, input().split())

# d = [[float("inf")]*n for _ in range(n)]

# for i in range(w):
#     x,y,z = map(int, input().split())
#     d[x][y] = z
#     d[y][x] = z
# # print(d)

# for j in range(n):
#     d[j][j] = 0
# print(warshall_floyd(d))

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n, w = map(int, input().split())

edges = []

d = [[float("inf")]*n for _ in range(n)]
for i in range(w):
    x,y,z = map(int, input().split())
    x -= 1
    y -= 1
    d[x][y] = z
    d[y][x] = z
    edges.append((x,y,z))

for i in range(n):
    d[i][i] = 0
print("d",d)

csr = csr_matrix(d)
dp = floyd_warshall(csr)
ans = 0
print("dp",dp)

for i, j, c in edges:
    print(i,j,c)
    if dp[i,j] < c:
        ans += 1
print(ans)



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