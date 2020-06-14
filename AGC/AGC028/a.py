N, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(N-1):
    if a[i] > x:
        break
    else:
        x -= a[i]
        ans += 1

if x == a[-1]:
    ans += 1
print(ans)