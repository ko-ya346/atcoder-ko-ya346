n, k, m, r = map(int, input().split())
S = sorted([int(input()) for _ in range(n-1)], reverse=True)
if n==k:
    S += [0]
sk = S[:k]
# 不足している点数
b = sum(sk)-k*r
if b >= 0:
    print(0)
# 最小値に不足分を足す
elif m < sk[k-1]-b:
    print(-1)
else:
    print(sk[-1]-b)
