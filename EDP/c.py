N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(100010)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k])
print(max(dp[N]))
#配るDP
# dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1] - h[i]))