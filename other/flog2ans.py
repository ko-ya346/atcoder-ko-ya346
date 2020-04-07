N, K = map(int, input().split())
*h, = map(int, input().split())
dp = [float("inf") for _ in range(N)]
dp[0] = 0
for i in range(N - 1):
    print("i=",i)
    for j in range(1, min(K + 1, N - i)):
        print("j=",j)
        print("dp[i+j]=",dp[i+j])
        print(abs(h[i + j] - h[i]))
        dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
print(dp[N - 1])