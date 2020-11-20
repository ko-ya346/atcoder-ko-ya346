import sys
read = sys.stdin.read

H, N = map(int, input().split())
m = map(int, read().split())
magic = zip(m, m)

dp = [10**9 for _ in range(H+10**4+1)]
dp[0] = 0

for a, b in magic:
    for j in range(H+1):
        if dp[j+a] > dp[j] + b:
            dp[j+a] = dp[j] + b

print(min(dp[H:]))