n = int(input())
G = [[] for _ in range(n)]

# 木グラフ
for _ in range(n-1):
    x, y = map(lambda x:int(x)-1, input().split())
    G[x].append(y)
    G[y].append(x)

# 訪問順リスト
S = []
# 出現位置
F = [0] * n
# 移動距離
depth = [0] * n

# euler tourの構築
# 二重辺の木を一筆書き
def dfs(v, d, past):
    F[v] = len(S)
    depth[v] = d
    S.append(v)

    for w in G[v]:
        if w != past:
            dfs(w, d+1, v)
            S.append(v)
dfs(0, 0, 0)
print(S)
print(F)
print(depth)
# 存在しない範囲は深さが他よりも大きくなるようにする 
INF = (n, None)

# LCAを計算するクエリの前計算
m = 2 * n
m0 = 2 ** (m-1).bit_length()
data = [INF]*(2*m0)
for i, v in enumerate(S):
    data[m0-1+i] = (depth[v], i)
print(data)

for i in range(m0-2, -1, -1):
    data[i] = min(data[2*i+1], data[2*i+2])
print(data)

# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield INF
    a += m0; b += m0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b-1]
        if a & 1:
            yield data[a-1]
            a += 1
        a >>= 1; b >>= 1

# LCAの計算 (外から呼び出す関数)
def query(u, v):
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv+1))[1]]

Q = int(input())
for i in range(Q):
    x, y = map(int,input().split())
    d = query(x-1, y-1)
    print(depth[x-1] + depth[y-1] - depth[d] * 2 + 1)
