N = int(input())
x = list(map(int, input().split()))

ans = float("inf")

l = []
for i in range(1, N+101):
    pow = 0
    for j in range(N):
        # print("x[j]", x[j])
        # print("i", i)
        # print((x[j]-i)**2)
        pow += (x[j]-i)**2
    # print(pow)
    if ans > pow:
        ans = min(ans, pow)
        l.append(i)

print(ans)
# print(l)