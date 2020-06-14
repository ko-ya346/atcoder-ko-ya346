def shortest_path(s, n, es):
    #s -> i　の最短経路
    #s: 始点、n: 頂点数、w:辺の数、es[i]: [辺の始点、辺の終点、辺のコスト]
    d = [float("inf")] * n
    #d[i]: s->iの最短距離
    d[s] = 0
    while True:
        update = False
        for p, q, r in es:
            #e: 辺iについて
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
        if not update:
            break
    return d

n,w = map(int,input().split()) #n:頂点数　w:辺の数
es = [] #es[i]: [辺の始点,辺の終点,辺のコスト]

for _ in range(w):
    x,y,z = map(int,input().split())
    es.append([x,y,z])
    es.append([y,x,z])

# print(shortest_path(0, n, es))

#負の経路の検出
def find_negative_loop(n, es):
    d = [float("inf")] * n
    d[0] = 0
    #始点はどこでもよい
    for i in range(n):
        for p, q, r in es:
            #e: 辺iについて
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                if i == n-1:
                    return True
    return False

# print(es)
print(find_negative_loop(n, es))