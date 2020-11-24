"""
コイントスをN回行うとき、
表または裏がK回以上連続で出る確率を求めよ
ex1
3 3
0.25

ex2
100 10
0.086659044348
"""

n, k = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1][1] = 1
for i in range(1, n):
    # サイコロをi回振ったとき
    for j in range(k):
        # j連続目
        if j+1<k:
            # k連続は数えてはいけないので捨てる
            dp[i+1][j+1] += dp[i][j]/2
        # 1連続から始める
        dp[i+1][1] += dp[i][j]/2
sum = 0
print(dp)
# 1~K回未満連続する確率の総和を1から引く
for i in range(k):
    sum += dp[n][i]
print(1-sum)