from collections import deque

H, W = map(int, input().split())

grid = [[-1]*W for _ in range(H)]

queue = deque([])

ans = 0

# while True:
#     f = 0
for i in range(H):
    s = input()
    for j, ss in enumerate(s):
        if ss =="#":
            queue.append((i, j))
            grid[i][j] = 0

#黒点をスタート地点とし、上下左右に移動した時の移動距離を記録していく
while queue:
    h, w = queue.popleft()
    for i in [h-1, h+1]:
            if i >= 0 and i < H:
                if grid[i][w] == -1:
                    grid[i][w] = grid[h][w]+1
                    queue.append((i, w))
    for j in [w-1, w+1]:
        if j >= 0 and j < W:
            if grid[h][j] == -1:
                grid[h][j] = grid[h][w]+1
                queue.append((h, j))

# print(grid)
print(max([max(b) for b in grid]))
