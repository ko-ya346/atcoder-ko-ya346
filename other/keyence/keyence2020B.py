N = int(input())
l = []

for _ in range(N):
    a, b =map(int, input().split())
    l.append((a-b, a+b))

l = sorted(l, key=lambda x:x[1])
start = l[0][1]
ans = 1

for i in range(1, N):
    # print(f"start{start}, ")
    if start <= l[i][0]:
        ans += 1
        start = l[i][1]
print(ans)