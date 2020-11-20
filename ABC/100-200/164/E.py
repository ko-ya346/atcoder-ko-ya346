N, M, S = map(int, input().split())

def shortest_path(s,n,w,es):
    #s→iの最短距離
    # s:始点, n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    #d[i] : s→iの最短距離
    d[s] = 0
    while True:
        update = False
        for p,q,s, r in es:
    # e: 辺iについて [from,to,cost]
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                pdate = True
        if not update:
            break
    return d

es = [] #es[i]: [辺の始点,辺の終点,辺のコスト]
for _ in range(M):
    u, v, a, b = map(int,input().split())
    es.append([u, v, a, b])
    es.append([v, u, a, b])

print(shortest_path(0,N,M*2,es))