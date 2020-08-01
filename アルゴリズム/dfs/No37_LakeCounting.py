H = 10
W = 12

G = [list(input()) for _ in range(H)]
# print(G)
ju = [[False for _ in range(W)] for _ in range(H)]
# print(ju)
que = [(0, 0)]
move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def dfs(x, y):
    if G[x][y] == ".":
        return
    # if ju[x][y]:
        # return

    G[x][y] = "."

    for xx, yy in move:
        if x+xx<0 or y+yy<0 or x+xx>=H or y+yy>=W:
            continue
        dfs(x+xx, y+yy)

cnt = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == "W":
            cnt += 1
            dfs(i, j)
print(G)
print(cnt)
'''
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.

'''