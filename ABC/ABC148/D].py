N = int(input())
a = list(map(int, input().split()))

ans = 0
n = 1

for i in a:
    if n == i:
        ans += 1
        n += 1

if ans:
    print(N-ans)
else:
    print(-1)