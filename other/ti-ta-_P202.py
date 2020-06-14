# donations = list(map(int, input().split()))
def f(donations):
    ans = 0

    N = len(donations)
    dp = [0 for _ in range(N)]

    for i in range(N-1):
        dp[i] = donations[i]
        if i > 0:
            dp[i] = max(dp[i], dp[i-1])
        if i > 1:
            dp[i] = max(dp[i], dp[i-2] + donations[i])
        ans = max(ans, dp[i])
    print(dp)
    for i in range(N-1):
        dp[i] = donations[i+1]
        if i > 0:
            dp[i] = max(dp[i], dp[i-1])
        if i > 1:
            dp[i] = max(dp[i], dp[i-2] + donations[i])
        ans = max(ans, dp[i])
    
    print(dp)
    print(ans)

l1 = [10, 3, 2, 5, 7,8]
l2 = [7, 7, 7, 7, 7, 7, 7]
l3 = [1,2,3,4,5,1,2,3,4,5]

f(l1)
f(l2)
f(l3)