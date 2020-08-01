import numpy as np
from numba import njit

N, K = map(int, input().split())
A = np.array((list(map(int, input().split()))), dtype=np.int64)

@njit
def imos(A):
    B = np.zeros(N, dtype=np.int64)
    for i,x in enumerate(A):
        a = max(0, i-x)
        b = min(i+x, N-1)
        B[a] += 1
        if b+1 <= N-1:
            B[b+1] -= 1
    B = np.cumsum(B)
    return B

for i in range(K):
    if i >= 50:
        break
    A = imos(A)
print(*A)