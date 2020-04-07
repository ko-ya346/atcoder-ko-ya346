n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [float("inf") for i in range(n)]
dp[0] = 0
for i in range(n-1):
    for j in range(1, min(k+1, n-i)):
        dp[i+j] = min(dp[i+j], dp[i]+abs(a[i+j]-a[i]))

print(dp[-1])