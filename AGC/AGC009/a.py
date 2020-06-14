N = int(input())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.reverse()
B.reverse()

ans = 0
before = 0

for i in range(N):
    mod = (A[i]+ans)%B[i]
    if mod != 0:
        ans += B[i]-mod

print(ans)