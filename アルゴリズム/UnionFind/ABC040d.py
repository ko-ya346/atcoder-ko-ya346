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

N, M = map(int, input().split())
road = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x:x[2], reverse=True)
Q = int(input())

uf = UnionFind(N)
ans = [None]*Q
query = sorted([list(map(int, input().split())) + [i] for i in range(Q)], key=lambda x:x[1], reverse=True)
# print(query)

#前回追加したところまでのindexを保持して
#木の追加に重複がないようにする
r_ind = 0
for v, w, i in query:
    while r_ind < M and road[r_ind][2] > w:
        a, b, y = road[r_ind]
        uf.union(a-1, b-1)
        r_ind += 1
    ans[i] = uf.size(v-1)

print(*ans, sep="\n")