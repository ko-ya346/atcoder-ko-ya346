N = int(input())

shogen = []

for _ in range(N):
    A = int(input())
    asho = []
    for i in range(A):
        x, y = map(int, input().split())
        asho.append((x-1, y))
    shogen.append(asho)
print(shogen)
ans = 0

for i in range(2**N):
    good = [0 for _ in range(N)]
    f = 1
    for j in range(N):
        if ((i >> j)&1):
            good[j] = 1
    print(f"good{good}")
    for k in range(N):
        print("k", k)
        if good[k]:
            for l, m in shogen[k]:
                print(f"l{l} m{m}")
                if good[l] != m:
                    f = 0
    print("f", f)
    if f:
        ans = max(ans, sum(good))

print(ans)