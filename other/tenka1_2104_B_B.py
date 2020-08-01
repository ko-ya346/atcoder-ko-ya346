N = int(input())
S = input()
mod = 10**9+7
T = []
for i in range(N):
    k = input()
    T.append((k, len(k)))

m = len(S)
dp = [0 for _ in range(m+1)]
dp[0] = 1

for i in range(m+1):
    for k, v in T:
        if S[i:i+v] == k:
            dp[i+v] += dp[i]
            dp[i+v] %= mod
    dp[i] %= mod
print(dp[-1])