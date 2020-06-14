import numpy as np
n, W = map(int, input().split())
dp = np.zeros((n,W+1), dtype='int64')

for i in range(n):
    w, v = map(int , input().split())

    #買わない選択肢を引き継ぐ
    dp[i, :w] = dp[i-1, :w]

    print(W-w+1)
    print(dp[i-1,:W-w+1]+v)
    dp[i, w:] = np.fmax(dp[i-1, w:], dp[i-1,:W-w+1]+v)
    # print(dp[i-1,:W-w+1]+v)
    print(dp)

    # print(dp[i])
print(dp[n-1][W])
