import numpy as np

N = int(input())
matrix = np.arange(N**2).reshape(N, N).astype("int8")
# print(matrix)
# for i in range(N):
#     for j in range(N):
#         matrix[i][j] = N*i+j

Q = int(input())

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 2:
        matrix[:, q[1]-1], matrix[:, q[2]-1] = matrix[:, q[2]-1], matrix[:, q[1]-1].copy()
    elif q[0] == 1:
        matrix[q[1]-1, :], matrix[q[2]-1, :] = matrix[q[2]-1, :], matrix[q[1]-1, :].copy()
    elif q[0] == 3:
        matrix = matrix.T
    else:
        print(matrix[q[1]-1, q[2]-1])
    # print(matrix)