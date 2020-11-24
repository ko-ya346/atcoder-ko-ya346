from bisect import bisect_right

n, t = map(int, input().split())
a = list(map(int, input().split()))
l = [0]
r = [0]
for x in a[:20]:
    for i in range(len(l)):
        l.append(x + l[i])
for x in a[20:]:
    for i in range(len(r)):
        r.append(x+r[i])
r.sort()

ans = 0
for x in l:
    if x > t:
        continue
    y = r[bisect_right(r, t-x) - 1]
    ans = max(ans, x + y)
print(ans)
