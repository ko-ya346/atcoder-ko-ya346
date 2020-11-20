N = int(input())
# N = 3
mod = 10**9+7

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(101)]
dp[0][3][3][3] = 1
# print(dp[0])

for len in range(N):
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                if dp[len][c1][c2][c3] == 0:
                    continue
                for a in range(4):
                    if a==2 & c1==1 & c2==0:
                        continue
                    if a==2 & c1==0 & c2==1:
                        continue
                    if a==1 & c1==2 & c2==0:
                        continue
                    if a==2 & c1==1 & c3==0:
                        continue
                    if a==2 & c2==1 & c3==0:
                        continue
                    dp[len+1][a][c1][c2] += dp[len][c1][c2][c3]
                    dp[len+1][a][c1][c2] %= mod

ans = 0
for c1 in range(4):
    for c2 in range(4):
        for c3 in range(4):
            ans += dp[N][c1][c2][c3]
            ans %= mod
print(ans)
# print(dp[N])