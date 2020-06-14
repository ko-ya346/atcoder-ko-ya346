import  numpy as np

N,W = map(int, input().split())

INF = float("inf")

dp = [INF] * (120 + 1)
dp = np.array(dp)

dp[0] = 0

for i in range(N):
    w, v = map(int, input().split())

    print("左辺", dp[:-v] + w)
    print("右辺",dp[v:])

    #同じ価値ならば重量が小さい方を記録する（minimum）
    dp[v:] = np.minimum(dp[:-v] + w , dp[v:])
    print(dp)


for v,num in enumerate(dp):
    if num <= W:
        ans = v

print(ans)
