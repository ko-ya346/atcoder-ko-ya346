N, K = map(int, input().split())
A = list(map(int, input().split()))

x = 0

for i in range(40, -1, -1):
    if 2**i + x > K:
        continue

    c = 0
    for a in A:
        if (a>>i)&1:
            c += 1

    if c <= N//2:
        x += 2**i

ans = 0
for a in A:
    ans += x^a

print(ans)