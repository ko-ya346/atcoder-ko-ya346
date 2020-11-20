N, A, B = map(int, input().split())
X= list(map(int, input().split()))

dp = [float("inf") for _ in range(N)]
dp[0] = 0

for i in range(N-1):
    dp[i+1] = min(dp[i]+(X[i+1]-X[i])*A, dp[i]+B)
print(dp[-1])