W, H = list(map(int, input().split()))
dp = [[0 for _ in range(H)] for _ in range(W)]

for i in range(W):
    for j in range(H):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
print(dp[W-1][H-1]%1000000007)