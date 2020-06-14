N = int(input())
A = sorted(list(map(int, input().split())))

a = [0]*(N+1)

for i in range(N):
    a[i+1] = a[i]+A[i]

A.reverse()
a.reverse()
# print(A)
# print(a)

ans = 1
for i in range(N):
    if A[i]/2 > a[i+1]:
        break
    ans += 1
print(ans)