def warshall_floyd(c):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    return c


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

cost = warshall_floyd(c)

ans = 0
for _ in range(h):
    a = list(map(int, input().split()))
    for i in a:
        if i > -1:
            ans += cost[i][1]
print(ans)