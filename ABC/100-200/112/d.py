x, y  = map(int, input().split())
mod = 10**9+7

def comb(n, r, mod):
    n1 = n+1
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer*(n1-i)%mod # combの分子
        denom = denom*i%mod #combの分母
    return numer*pow(denom, mod-2, mod)%mod #(n!*(r**(mod-2)%mod))%mod
    #a/b mod p = (a*(1/b) mod p)なので1/b(b**-1)を求めたい（つまりcombの分母）
    #(b**(p-2)*b mod p) = 1 なので
    #b**-1 = b**-2 mod p　が成立！！！
    #return内のpowがb**-1を求める部分

if (x+y)%3 != 0 or (2*x-y)//3 < 0 or (2*y-x)//3 < 0:
    print(0)
else:
    n = (2*x-y)//3
    m = (2*y-x)//3
    print(comb(n+m, min(n, m), mod))


#TLE解
# from collections import deque

# X, Y = map(int, input().split())

# knight = [(1, 2), (2, 1)]
# dp = [[0 for _ in range(Y+1)] for _ in range(X+1)]
# dp[0][0] = 1

# que = deque([(0, 0)])

# while que:

#     x, y = que.pop()
#     for x1, y1 in knight:
#         if x+x1 > X or y+y1 > Y:
#             continue
#         dp[x+x1][y+y1] += dp[x][y]
#         que.append((x+x1, y+y1))
#     # print(que)
# print(dp[X][Y]%1000000007)
# # print(dp)