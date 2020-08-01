import numpy as np
N, W = map(int, input().split())
dp = np.zeros((N, W+1), dtype='int64')

for i in range(N):
    w, v = map(int , input().split())

    #買わない選択肢を引き継ぐ
    dp[i, :w] = dp[i-1, :w]
    print("1", dp[i, :w])
    print("2", W-w+1)
    print("3", dp[i-1,:W-w+1]+v)
    dp[i, w:] = np.fmax(dp[i-1, w:], dp[i-1,:W-w+1]+v)
    # print(dp[i-1,:W-w+1]+v)
    print(dp)

    # print(dp[i])
print(dp[N-1][W])
