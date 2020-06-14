N = int(input())
p = list(map(int, input().split()))

max_n = p[0]
min_n = p[0]
ans = 1

for i in range(1, N):
    # print("max", max_n, "min", min_n,"p[i]", p[i])
    if min_n >= p[i]:
        ans += 1
        min_n = p[i]
    # else:
        # max_n = p[i]

print(ans)