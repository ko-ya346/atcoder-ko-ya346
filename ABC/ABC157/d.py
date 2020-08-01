# https://note.nkmk.me/python-union-find/

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M, K = map(int, input().split())
par = [-1]*N
#直接友達になっている人数とブロックしている人数をカウント
num = [0]*N

uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    #友達関係をつなげる
    uf.union(a, b)
    #直接友達なのでカウントする
    num[a] += 1
    num[b] += 1

for _ in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    # print(f"c{c}, d{d}, uf.same(c, d) {uf.same(c, d)}")
    #同じグループに属している場合、size()にカウントされるのでnumを増やす
    if uf.same(c, d):
        num[c] += 1
        num[d] += 1
# print(num)
for i in range(N):
    #直接友達関係の人と同じグループでブロックしている人、自分自身を除く人数が候補となる
    print(uf.size(i)-1-num[i], end=" ")