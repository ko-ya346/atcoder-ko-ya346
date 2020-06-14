import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))

def imos(A):
    B = np.zeros_like(A)
    for i,x in enumerate(A):
        a = max(0, i-x)
        b= min(i+x, N-1)
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