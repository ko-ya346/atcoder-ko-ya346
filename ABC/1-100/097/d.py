class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            # 要素が0以下は親
            return x
        else:
            #  
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #xのグループとyのグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 既に親が同じ場合は何もしない
        if x == y:
            return

        # 高い方の木を親とする
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 新たに繋ぐ木の高さを加える
        self.parents[x] += self.parents[y]
        # 親を要素に入れる
        self.parents[y] = x

    #xのグループのサイズ
    def size(self, x):
        return -self.parents[self.find(x)]

    #xとyが同じグループかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

n, m = map(int, input().split())
p = list(map(int, input().split()))

uf = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

ans = 0
for i in range(n):
    if uf.same(p[i]-1, i):
        ans += 1

print(ans)