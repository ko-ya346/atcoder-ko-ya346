def dfs(x, y):
    if x < 0 or y < 0 or x >= H or y >= W:
        return 
    if maze[x][y] == "#":
        return
    if judge[x][y]:
        return
    judge[x][y] = 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
H, W = map(int, input().split())
maze = []

for i in range(H):
    row = list(input())
    if "s" in row:
        start = (i, row.index("s"))
    if "g" in row:
        goal = (i, row.index("g"))
    maze.append(row)

judge = [[False] * W for _ in range(H)]
dfs(start[0], start[1])

if judge[goal[0]][goal[1]]:
    print("Yes")
else:
    print("No")