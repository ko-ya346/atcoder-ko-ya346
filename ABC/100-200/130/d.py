N, K = map(int, input().split())
A = list(map(int, input().split()))

a = [0 for _ in range(N+1)]

for i in range(N):
    a[i+1] = A[i]+ a[i]

num = 0
ans = 0

for i in range(N):
    num += a[i]
    if num >= K:
        ans += N-i
        num = 0

a.reverse()
for i in range(N):
    num += a[i]
    if num >= K:
        ans += 1
        num = 0

print(ans)