N = int(input())
A = sorted(list(map(int, input().split())))

m_a = max(A)+1
dp = [0]*m_a

for i in A:
    dp[i] += 1
    if dp[i]==1:
        for j in range(i*2, m_a, i):
            dp[j] += 2
    # print(dp)
print(dp.count(1))