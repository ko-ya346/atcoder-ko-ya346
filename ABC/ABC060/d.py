N, W = map(int, input().split())
obj = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(W)] for _ in range(N)]

dp[0][0] = 0

for i in range(N):
    w, v = obj[i]
    if 