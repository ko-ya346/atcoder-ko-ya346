import numpy as np

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))

f = 0
if np.max(A) > K:
    for i in range(N):
        num = A[i]
        if num == 0:
            continue
        A %= A[i]
        A[i] = num
        if np.any(A == 1):
            f = 1
            break

if f:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")