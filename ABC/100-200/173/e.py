# https://note.nkmk.me/python-union-find/

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

    #xとyが同じグループかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
p = list(map(int, input().split()))

uf = UnionFind(N)

for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x-1, y-1)

ans = 0
for i in range(N):
    if uf.same(i, p[i]-1):
        ans += 1
print(ans)