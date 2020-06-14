N = int(input())
t = [int(input()) for _ in range(N)]

ans = float("inf")

for i in range(2**N):
    a1, a2 = 0, 0
    for j in range(N):
        # print(i >> j)
        if ((i >> j)&1):
            a1 += t[j]
        else:
            a2 += t[j]
    # print(a1, a2)
    ans = min(ans, max(a1, a2))
print(ans)