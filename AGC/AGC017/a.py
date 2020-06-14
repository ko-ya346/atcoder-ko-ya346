n, p = map(int, input().split())
A = list(map(int, input().split()))

f = 0
for a in A:
    if a%2:
        f = 1
        break

if f:
    ans = 2**(n-1)
else:
    if p:
        ans = 0
    else:
        ans = 2**n
print(ans)