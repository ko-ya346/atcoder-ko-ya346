#treeDP

mod = 10 ** 9 + 7

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

E = [[] for _ in range(N + 1)]
for a, b in AB:
    E[a].append(b)
    E[b].append(a)

# print(E)
def dfs(cur, par):
    #1に到達したら終わり
    w = b = 1
    #次の島
    for nxt in E[cur]:
        if nxt == par:
            continue
        #根から求める
        nw, nb = dfs(nxt, cur)
        #w: 注目する頂点が白or黒の時
        w = (w * (nw + nb)) % mod
        #注目する頂点が黒のとき
        b = (b * nw) % mod
    return w, b
# print(b)
w, b = dfs(1, -1)
print((w + b) % mod)
