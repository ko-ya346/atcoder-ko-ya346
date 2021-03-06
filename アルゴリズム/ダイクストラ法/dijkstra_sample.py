def dijkstra(s, n, w, cost):
    #始点sから各頂点への最短距離
    #n:頂点数、w:辺の数、cost[u][v]:辺uvのコスト（存在しない時はinf)
    d = [float("inf")]*n
    used = [False]*n
    d[s] = 0

    while True:
        v = -1
        #まだ使われていない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and d[i]< d[v]:
                v = i
        if v == -1:
            break
        used[v] =True
        for j in range(n):
            d[j] = min(d[j], d[v]+cost[v][j])
    return d

n, w = map(int, input().split())
cost = [[float("inf") for _ in range(n)] for _ in range(n)]

for _ in range(w):
    x, y, z = map(int, input().split())
    cost[x][y] = z
    cost[y][x] = z
print(dijkstra(0, n, w, cost))


'''
4 4
1 2 100
2 3 250
2 4 200
3 4 100

'''