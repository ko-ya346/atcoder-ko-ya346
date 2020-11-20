def find_positive_loop(n, es):
    d = [-float("inf")] * n
    d[0] = 0
    #始点はどこでもよい
    for i in range(n):
        for p, q, r in es:
            #e: 辺iについて
            if d[p] != -float("inf") and d[q] < d[p] + r:
                d[q] = d[p] + r
                if i == n-1:
                    return True
    return False

def longest_path(s, n, es):
    #s -> i　の最短経路
    #s: 始点、n: 頂点数、w:辺の数、es[i]: [辺の始点、辺の終点、辺のコスト]
    d = [-float("inf")] * n
    #d[i]: s->iの最短距離
    d[s] = 0
    while True:
        update = False
        for p, q, r in es:
            #e: 辺iについて
            if d[p] != -float("inf") and d[q] < d[p] + r:
                d[q] = d[p] + r
                update = True
        if not update:
            break
    return d


n,w = map(int,input().split()) #n:頂点数　w:辺の数
es = [] #es[i]: [辺の始点,辺の終点,辺のコスト]

for _ in range(w):
    x,y,z = map(int,input().split())
    es.append([x-1,y-1,z])
    # es.append([y-1,x-1,z])

# print(es)
# print(find_positive_loop(n,es))


if find_positive_loop(n,es):
    print("inf")
else:
    print(max(longest_path(0, n, es)))