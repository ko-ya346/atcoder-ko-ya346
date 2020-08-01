N = 4
obj = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5
sumW = 8

dp = [[-1 for _ in range(10)] for _ in range(N)]
dp[0][0] = 0

for i in range(N-1):
    for j in range(W+1):
        if j < obj[i][0]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-obj[i][0]]+obj[i][1])
print(dp)

#---------------------------------------------------------------------
#別解　同じ配列を再利用
N = 4
obj = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5
sumW = 8

dp = [-1 for _ in range(9)]
dp[0] = 0

for i in range(N):
    for j in range(W, obj[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-obj[i][0]]+obj[i][1])

print(dp)