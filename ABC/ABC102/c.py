N  = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = A[i]-i-1

b = sorted(A)[N//2]

ans = 0
for i in range(N):
    ans += abs(A[i]-(b))
print(ans)