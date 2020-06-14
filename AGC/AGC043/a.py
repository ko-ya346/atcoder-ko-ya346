H, W = map(int, input().split())

dp = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if dp[i][j] == ".":
            dp[i][j] = 0
        else:
            dp[i][j] = 1

for i in range(W-1):
    dp[0][i+1] += dp[0][i]

for j in range(H-1):
    dp[j+1][0] += dp[j][0]

for i in range(1, H):
    for j in range(1, W):
        dp[i][j] += min(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])