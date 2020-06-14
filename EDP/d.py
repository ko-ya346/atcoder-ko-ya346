N, W = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

sum_v = 0

for _, v in L:
    sum_v += v

dp = [-1]*100010
dp[0] = 0
for w, v in L:
    for i in range(sum_v-v, -1, -1):
        if dp[i] == -1:
            continue
        if dp[i+v] < dp[i] + w:
            dp[i+v] = dp[i] + w

ans = 0
for i, a in enumerate(dp):
    if a <= W:
        ans = max(ans, i)

print(i)