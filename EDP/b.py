N, K = map(int, input().split())
h = list(map(int, input().split())) + [0]*101010

dp = [float("inf")]*101010
dp[0] = 0

for i in range(N):
    for k in range(1, K+1):
        dp[i+k] = min(dp[i+k], dp[i] + abs(h[i+k] - h[i]))
    # print(dp)
print(dp[N-1])