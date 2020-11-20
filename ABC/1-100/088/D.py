from collections import deque

H, W = map(int, input().split())
black = 0
s = ["#" * (W+2)]
for _ in range(H):
    row = input()
    black += row.count("#")
    s.append("#" + row + "#")
s.append("#" * (W+2))

def bfs(x, y):
    if s[x][y] == "#":
        return 0
    queue = deque([(x, y)])
    dist = [[-1]*(W+2) for _ in range(H+2)]
    dist[x][y] = 0
    while queue:
        r, c = queue.popleft()
        d = dist[r][c]
        for i in [r-1, r+1]:
            if i >= 0 and i <= H:
                if s[i][c] == "." and dist[i][c] == -1:
                    dist[i][c] = d+1
                    queue.append((i, c))
        for j in [c-1, c+1]:
            if j >= 0 and j <= W:
                if s[r][j] == "." and dist[r][j] == -1:
                    dist[r][j] = d+1
                    queue.append((r, j))
    return dist
ans = bfs(1,1)[-2][-2]
if ans != -1:
    print(H*W-bfs(1,1)[-2][-2]-1-black)
else:
    print(-1)