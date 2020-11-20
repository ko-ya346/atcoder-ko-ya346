def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

n, m = map(int, input().split())

d = [[float("inf")]*n for _ in range(n)]

for _ in range(m):
    x,y,z = map(int, input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z

for j in range(n):
    d[j][j] = 0

l = warshall_floyd(d)

ans = float("inf")
for i in range(n):
    ans = min(ans, max(l[i]))
print(ans)