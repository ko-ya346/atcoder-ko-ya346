x, n = map(int, input().split())
if n == 0:
    print(x)
else:
    p = sorted(list(map(int, input().split())))

    ans = [10**4, 10**4]
    for i in range(102):
        if i not in p:
            if ans[1] == abs(x-i):
                ans[0] = min(ans[0], i)
            elif ans[1] > abs(x-i):
                ans[0] = i
                ans[1] = abs(x-i)
    print(ans[0])

