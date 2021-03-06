from collections import Counter, defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xのグループとyのグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # xのグループのサイズ
    def size(self, x):
        return -self.parents[self.find(x)]

    # xとyが同じグループかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

n, q = map(int, input().split())
member = [defaultdict(int) for _ in range(n)]
for i, c in enumerate(map(int, input().split())):
    member[i][c-1] = 1

uf = UnionFind(n)

for _ in range(q):
    p, a, b = map(lambda x: int(x)-1, input().split())
    if p:
        print(member[uf.find(a)][b])
    else:
        a = uf.find(a)
        b = uf.find(b)
        if a == b:
            continue
        if uf.parents[a] > uf.parents[b]:
            a, b = b, a
        uf.union(a, b)

        for k, v in member[b].items():
            member[a][k] += v
