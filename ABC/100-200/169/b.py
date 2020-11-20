N = int(input())
a = list(map(int, input().split()))

ans = 1
if 0 in a:
    print(0)
else:
    for i in a:
        ans *= i
        if ans > 1000000000000000000:
            print(-1)
            exit()

    print(ans)