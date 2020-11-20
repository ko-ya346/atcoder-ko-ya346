H, N = map(int, input().split())
magic = [list(map(int, input().split())) for _ in range(N)]

dp = [10**9 for _ in range(H+10**4+1)]
dp[0] = 0

for a, b in magic:
    for j in range(H+1):
        if dp[j+a] > dp[j] + b:
            dp[j+a] = dp[j] + b

print(min(dp[H:]))