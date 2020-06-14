N, K = map(int, input().split())
A = list(map(int, input().split()))

a = [0 for _ in range(N+1)]

for i in range(N):
    a[i+1] = A[i]+ a[i]

l, r = 0, 1
ans = 0

while l != N:
    # print(l, r)
    if a[r]-a[l] < K:
        if r == N:
            break
        else:
            r += 1
    else:
        ans += N-r+1
        l += 1

print(ans)