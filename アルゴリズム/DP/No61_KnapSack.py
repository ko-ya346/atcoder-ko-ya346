N = 3
obj = [(3, 4), (4, 5), (2, 3)]
W = 7
sumW = 9

dp = [[-1 for _ in range(10)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        if j < obj[i][0]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-obj[i][0]]+obj[i][1])
print(dp)

#---------------------------------------------------------------------
#別解　同じ配列を再利用

N = 3
obj = [(3, 4), (4, 5), (2, 3)]
W = 7
sumW = 9

dp = [-1 for _ in range(10)]
dp[0] = 0

for i in range(N):
    for j in range(obj[i][0], W+1):
        dp[j] = max(dp[j], dp[j-obj[i][0]]+obj[i][1])

print(dp)
