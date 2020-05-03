from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cl = [input() for _ in range(R)]

def bfs(x, y):
    if cl[y][x] == "#":
        return 0
    queue = deque([(y, x)])
    dist = [[-1]*(C) for _ in range(R)]
    dist[y][x] = 0
    while queue:
        r, c = queue.popleft()
        d = dist[r][c]
        for i in [r-1, r+1]:
            if cl[i][c] == "." and dist[i][c] == -1:
                dist[i][c] = d+1
                queue.append((i, c))
        for j in [c-1, c+1]:
            if cl[r][j] == "." and dist[r][j] == -1:
                dist[r][j] = d+1
                queue.append((r, j))
    return dist

print(bfs(sy-1, sx-1)[gy-1][gx-1])