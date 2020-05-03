import pdb
import sys
sys.setrecursionlimit(10**7)
F = sys.stdin
 
H,W = map(int,F.readline().split())
a = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if a[i][j]== "s":
            s1 = i
            s2 = j
        if a[i][j]== "g":
            g1 = i
            g2 = j

judge = [[False]*W for b in range(H)]

def dfs(h, w):
    if h < 0 or h >= H or w < 0 or w >= W:
        return
    if a[h][w] == '#':
        return
    if judge[h][w]:
        return
    judge[h][w] = True
    dfs(h+1, w)
    dfs(h-1, w)
    dfs(h, w+1)
    dfs(h, w-1)

dfs(s1, s2)
if judge[g1][g2]:
    print('Yes')
    sys.exit()
print('No')