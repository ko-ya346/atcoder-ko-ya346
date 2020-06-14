N = int(input())
p = list(map(float, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
# dp[0][0] = 1-p[0]
# dp[0][1] = p[0]

for i in range(N):
    for j in range(i+1):
        # print(f"i {i}, j {j}")
        # print(f"p[i] {p[i]}, dp[i][j] {dp[i][j]}")

        if i == 0:
            dp[i+1][j] += 1-p[i]
            dp[i+1][j+1] += p[i]
        else:
            dp[i+1][j] += (1-p[i])*dp[i][j]
            dp[i+1][j+1] += p[i]*dp[i][j]
        # print("dp", dp)

ans = 0
for i, v in enumerate(dp[-1]):
    if i > N//2:
        ans += v

print(ans)