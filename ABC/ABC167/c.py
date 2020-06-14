import numpy as np

N, M, X = map(int, input().split())

C = np.array([list(map(int, input().split())) for _ in range(N)])

cost = float("inf")

for i in range(2**N):
    buy = np.zeros(M+1)
    for j in range(N):
        if ((i >> j)&1):
            buy += C[j]
        if np.all(buy[1:] >= X):
            cost = min(cost, buy[0])

if cost == float("inf"):
    print(-1)
else:
    print(int(cost))