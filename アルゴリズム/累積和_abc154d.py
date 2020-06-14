N, K = map(int, input().split())
p = list(map(int, input().split()))

a = [0 for _ in range(N+1)]

for i in range(N):
    a[i+1] = (1+p[i])/2 + a[i]

ans = 0

for i in range(N-K+1):
    ans = max(ans, a[i+K]-a[i])

# print(a)
print(ans)