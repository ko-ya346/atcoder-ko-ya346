from collections import deque
INF = 0xffffffff
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

H, W = map(int, input().split())
warp = [list() for i in range(26)]
que = deque([])

grid = []
for y in range(H):
    row = list(input())
    for x in range(W):
        if row[x].islower():
            warp[ord(row[x]) - 97].append((y, x))
        elif row[x] == "S":
            sy, sx = (y, x)
            que.append((y, x))
        elif row[x] == "G":
            ty, tx = (y, x)
    grid.append(row)

cost = [[INF for _ in range(W)] for _ in range(H)]
cost[sy][sx] = 0

while que:
    y, x = que.popleft()
    c2 = cost[y][x]+1
    
    for d in range(4):
        x2 = x+dx[d]
        y2 = y+dy[d]

        if x2 < 0 or x2 >= W or y2 < 0 or y2 >= H or grid[y2][x2] == "#":
            continue
        if cost[y2][x2] > c2:
            cost[y2][x2] = c2 
            que.append((y2, x2))

    if grid[y][x].islower():
        t = ord(grid[y][x])-97
        for wy, wx in warp[t]:
            if cost[wy][wx] > c2:
                cost[wy][wx] = c2    
                que.append((wy, wx))
        warp[t].clear()

ans = cost[ty][tx]
if ans==INF:
    print(-1)
else:
    print(ans)
