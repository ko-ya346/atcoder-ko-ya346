n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n-1):
    diff = a[i] - a[i+1]
    if diff > 0:
        ans += diff
        a[i+1] += diff

print(ans)