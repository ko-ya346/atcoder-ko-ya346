N = int(input())
D = list(map(int, input().split()))

M = int(input())
T = list(map(int, input().split()))

d = [0 for _ in range(200005)]
t = [0 for _ in range(200005)]

ans = "YES"

for i in range(N):
    d[D[i]] += 1

for i in range(M):
    t[T[i]] += 1

for i in range(len(d)):
    if t[i] > d[i]:
        ans = "NO"

print(ans)
