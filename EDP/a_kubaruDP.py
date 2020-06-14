N = int(input())
h = list(map(int, input().split())) + [0]*100010

dp = [float("inf")]*100010
dp[0] = 0

for i in range(N):
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1] - h[i]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(h[i+2] - h[i]))
    # print(dp)
print(dp[N-1])
