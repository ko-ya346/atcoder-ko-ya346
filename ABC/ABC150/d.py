N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 10**9+7

for i in A:
    cnt = 0
    while i%2 == 0:
        cnt += 1
        i //= 2
    ans= min(ans, cnt)
print(ans)

