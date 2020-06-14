N, W = map(int, input().split())

weight = []
value = []

for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (W+1)]*(N+1)

for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-weight[i]] + value[i])
        # else:
        dp[i+1][w] = max(dp[i+1][w], dp[i][w])
        print("i", i, "w", w)
        print(dp)

print(dp[N])
# print(weight)
# print(value)