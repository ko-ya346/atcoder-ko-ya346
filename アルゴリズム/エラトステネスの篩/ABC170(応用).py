N = int(input())
A = sorted(list(map(int, input().split())))
n = 10**6+1

dp = [0 for _ in range(max(A)+1)]

for i in A:
    dp[i] += 1
    if dp[i]==1:
        for j in range(i*2, max(A)+1, i):
            dp[j] = 2
    # print(dp)
print(dp.count(1))