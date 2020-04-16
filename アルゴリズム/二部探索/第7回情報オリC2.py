import bisect

N,M=map(int, input().split())
point = [0]+[int(input()) for _ in range(N)]

s = set()
for i in range(N+1):
    for j in range(i, N+1):
        s.add(point[i]+point[j])

l =sorted(list(s))

x = 0
for k in range(len(l)):
    if l[k] > M:
        continue
    else:
        x = max(x, l[k]+l[bisect.bisect_left(l,M-l[k])-1])
print(x)