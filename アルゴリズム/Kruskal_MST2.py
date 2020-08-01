from heapq import *
#->: 型注釈
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #xのグループとyのグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

N = int(input())
X = []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, y, i))

X.sort(key=lambda x: x[0])

H = []
heapify(H)
for i in range(N-1):
    x1, j1 = X[i][0], X[i][2]
    x2, j2 = X[i+1][0], X[i+1][2]
    heappush(H,(x2-x1, j1, j2))

X.sort(key=lambda x: x[1])

for i in range(N-1):
    y1, j1 = X[i][1], X[i][2]
    y2, j2 = X[i+1][1], X[i+1][2]
    heappush(H,(y2-y1, j1, j2))

ans = 0

uf = UnionFind(N)
while H:
    w,s,t = heappop(H)
    if uf.find(s) != uf.find(t):
        uf.union(s,t)
        ans += w
print(ans)