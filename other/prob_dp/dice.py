'''
サイコロをN回振る時、
出た目の数の和がK以上になる確率
ex1
1 4
0.5

ex2
3 5
0.981481481481
'''
# i回サイコロを振った時、
# 出た目の数の和がjになる確率を状態として持つ
n, K = map(int, input().split())
dp = [[0 for _ in range(n*6+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(K):
        for k in range(1, 7):
            dp[i+1][min(K, j+k)] += dp[i][j] / 6
print(dp)
print(dp[n][K])
