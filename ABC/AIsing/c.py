N = int(input())

ans = [0 for _ in range(N)]

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            n = x**2+y**2+z**2+x*y+y*z+z*x
            if n <= N:
                ans[n-1] += 1


print(*ans, sep="\n")