import numpy as np
n, W = map(int, input().split())
sina = []

for _ in range(n):
    w, v = map(int , input().split())
    sina.append((w, v))

sum_v = np.sum(np.array(sina), axis=0)[1]
dp = np.zeros((n, sum_v))

for i, (w, v) in enumerate(sina):
    #買わない選択肢を引き継ぐ
    print(dp)
    dp[i, :v] = dp[i-1, :v]
    print(dp)

    print(sum_v-v+1)
    print(dp[i-1,:sum_v-v+1]+w)
    dp[i, v:] = np.fmax(dp[i-1, v:], dp[i-1,:sum_v-v]+w)
    # print(dp[i-1,:W-w+1]+v)
    print(dp)

    # print(dp[i])
ans = np.where(dp[-1] < W)
print(np.max(ans)+1)
