n = int(input())
a = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    if i >= 2:
        dp[i] = min(dp[i-1]+abs(a[i]-a[i-1]), dp[i-2]+abs(a[i]-a[i-2]))
    elif i == 1:
        dp[i] = abs(a[i]-a[i-1])
    print(dp)
print(dp[-1])