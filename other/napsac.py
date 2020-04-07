N, W = map(int, input().split())
w, v = [0] * N, [0] * N
for i in range(N):
	w[i], v[i] = map(int, input().split())
print("w=", w)
print("v=", v)
dp = [[0] * (W + 1) for _ in range(N + 1)]
# dp[i][j](j=0,1,...,W)の値が求まっている状態で、dp[i+1][j]を更新することを考える
for i in range(N):
    for j in range(W + 1):
        # 品物(w[i],v[i])を選ぶとき、j-w[i]>=0に限って、価値v[i]が加算される
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])
        # 品物(w[i],v[i])を選ばないとき、何も加算しない
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        print(dp)

print(dp[N][W])