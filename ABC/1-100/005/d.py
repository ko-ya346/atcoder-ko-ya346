from itertools import accumulate
N = int(input())

# Dの二次元累積和
D = [None] * (N+1)
D[0] = [0] * (N+1)

for i in range(N):
    D[i+1] = [0] + [*accumulate(list(map(int, input().split())))]

for i in range(N):
    for j in range(N+1):
        D[i+1][j] += D[i][j]

# index:たこ焼きの個数, value:最大おいしさ
cnt = [0] * (N**2+1)
for a in range(N+1): # y座標の上端
    for b in range(N+1): # x座標の左端
        for c in range(a+1, N+1): # y座標の下端
            for d in range(b+1, N+1): # x座標の右端
                res = D[c][d] - D[a][d] - D[c][b] + D[a][b]
                # print(f"D[c][d], {D[c][d]}")
                # print(f"D[a][d], {D[a][d]}")
                # print(f"D[c][b], {D[c][b]}")
                # print(f"D[a][b], {D[a][b]}")
                res = D[c][d] - D[a][d] - D[c][b] + D[a][b]
                s = (c-a) * (d-b)
                cnt[s] = max(cnt[s], res)
Q = int(input())
for i in range(Q):
    P = int(input())
    print(max(cnt[:P+1]))