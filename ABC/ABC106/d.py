N, M, Q = map(int, input().split())

LR = [[0 for _ in range(N)] for _ in range(N)]
LRsum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    l, r = map(int, input().split())
    LR[l-1][r-1] += 1

# for i in LR:
#     print(i)

#二次元累積和
for i in range(N):
    for j in range(N):
        LRsum[i+1][j+1] = LRsum[i][j+1] + LRsum[i+1][j] - LRsum[i][j] + LR[i][j]

# print(LRsum)

for _ in range(Q):
    p, q = map(int, input().split())
    print(LRsum[q][q]-LRsum[q][p-1]-LRsum[p-1][q]+LRsum[p-1][p-1])

# print(L)
# print(LL)