N, x = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    if a[i]+a[i+1] > x:
        if -a[i]+x > 0:
            ans += a[i+1]+a[i]-x
            a[i+1] = x-a[i]
        else:
            ans += a[i+1]
            a[i+1] = 0
            ans += a[i]-x
            a[i] -= a[i]-x

    # print(i)
    # print(a)
    # print(ans)

print(ans)