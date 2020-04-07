n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(3)] for j in range(n)]
dp[0]= a[0]

for i in range(n-1):
    dp[i+1][0] = max(dp[i+1][0], dp[i][1]+a[i+1][0], dp[i][2]+a[i+1][0])
    print(dp)
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]+a[i+1][1], dp[i][2]+a[i+1][1])
    print(dp)
    dp[i+1][2] = max(dp[i+1][2], dp[i][0]+a[i+1][2], dp[i][1]+a[i+1][2])
    print(dp)

print(max(dp[n-1]))