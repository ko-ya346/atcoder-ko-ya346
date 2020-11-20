N = int(input())
XY = [tuple(int(x) for x in input().split()) for _ in range(N-1)]
Q = int(input())
AB = [tuple(int(x) for x in input().split()) for line in range(Q)]

graph = [[] for _ in range(N+1)]
for x,y in XY:
    graph[x].append(y)
    graph[y].append(x)

par = [[0] * 20 for _ in range(N+1)] # 2^i個上
depth = [0] * (N+1) # 根からの距離

q = [1]
while q:
    x = q.pop()
    p = par[x][0]
    depth[x] = depth[p] + 1
    for n in range(19):
        par[x][n+1] = par[par[x][n]][n]
    for y in graph[x]:
        if y == p:
            continue
        par[y][0] = x
        q.append(y)

def LCA(x,y,par,depth):
    dx = depth[x]
    dy = depth[y]
    if dx > dy:
        dx,dy = dy,dx
        x,y = y,x
    n = dy - dx
    while n:
        m = n&(-n)
        i = m.bit_length()-1
        y = par[y][i]
        n -= m
    if x == y:
        return x
    for t in range(19,-1,-1):
        px = par[x][t]
        py = par[y][t]
        if px == py:
            continue
        x = px
        y = py
    return par[x][0]

answer = [1 + depth[x] + depth[y] - 2*depth[LCA(x,y,par,depth)] for x,y in AB]

print('\n'.join(map(str,answer)))