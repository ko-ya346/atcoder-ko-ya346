N, T = map(int, input().split())

A = []
sum_aoki = 0

for _ in range(N):
    a, b = map(int, input().split())
    sum_aoki += b
    A.append((a, b, a-b))

ans = N

A.sort(key=lambda x:x[2])
# print(A)

for i, v, _ in A:
    # print("i", i, "v", v)
    if sum_aoki-v+i <= T:
        sum_aoki += i-v
        ans -= 1
    # print("sum", sum_aoki)

if sum_aoki > T:
    print(-1)
else:
    print(ans)
