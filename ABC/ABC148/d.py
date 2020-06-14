# def g1(n, p):
#     if n == 0:
#         return 0
#     return n/p + g1(n/p, p)


# def g2(n, p):
#     if n%2 == 1:
#         return g1(n, p) - g2(n-1, p)
#     res = g1(n/2, p)
#     if p == 2:
#         res += n/2
#     return res
# ans = min(g2(N, 2), g2(N, 5))

N = int(input())
if N%2 == 1:
    print(0)
else:
    ans = 0
    N //= 2
    while N:
        ans += N//5
        N //= 5

    print(ans)