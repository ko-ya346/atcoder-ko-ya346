# from itertools import permutations

# N, M = map(int, input().split())
# audience = [list(map(int, input().split())) for _ in range(M)]

# ans = 0
# for ranking in list(permutations(range(1, N+1), N)):
#     f = 1
#     for x, y in audience:
#         # print(ranking, x, y)
#         if ranking.index(x) > ranking.index(y):
#             f = 0
#             break
#     ans += f

# print(ans)


N, M = map(int, input().split())
D = {i: 0 for i in range(N)}
for i in range(M):
    x, y = map(int, input().split())
    D[x-1] += 1<<(y-1)

# 1<<N == 2**N
dp = [0 for i in range(1<<N)]
dp[0] = 1
print(D)
def abc041d(bit):
    if dp[bit] != 0:
        return dp[bit]
    val = 0
    for i in range(N):
        if (1<<i) & (bit):
            flg = True
            for j in range(N):
                if j != i and (bit >> j) & 1:
                    if (1 << j) & D[i]:
                        flg = False
            val += flg * abc041d(bit&(~(1<<i)))
    dp[bit] = val
    return dp[bit]
v = abc041d((1<<N) - 1)
print(dp[(1<<N) - 1])
