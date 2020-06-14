N = int(input())

A = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*N]*N

for i in range(N):
    dp[0][i]