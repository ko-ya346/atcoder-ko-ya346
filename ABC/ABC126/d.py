import sys
input = sys.stdin.buffer.readline
#再帰回数の上限を変更、記入しないとREが発生する場合がある
sys.setrecursionlimit(10**9)

N = int(input())
# v = [list(map(int, input().split())) for _ in range(N-1)]

edge = [[] for _ in range(N)]

for i in range(N-1):
    v1, v2, w = map(int, input().split())
    edge[v1-1].append((v2-1, w))
    edge[v2-1].append((v1-1, w))

color = [-1 for _ in range(N)]
color[0] = 1

def dfs(x):
    for v, w in edge[x]:
        if color[v] == -1:
            color[v] = (w + color[x])%2
            dfs(v)



dfs(0)
print(*color, sep="\n")