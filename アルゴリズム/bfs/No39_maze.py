H = 10
W = 10

maze = []

for i in range(H):
    m = list(input())
    if "S" in m:
        sx, sy = i, m.index("S")
    if "G" in m:
        gx, gy = i, m.index("G")
    maze.append(m)
# print(sx, sy, gx, gy)

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
maze[sx][sy] = 0
maze[gx][gy] = "."
que = [(sx, sy)]

while que:
    x, y = que.pop(0)
    # print(maze[x][y])
    if x == gx and y == gy:
        print(maze[x][y])
        break
    for xx, yy in move:
        if x+xx<0 or x+xx>=H or y+yy<0 or y+yy>=W:
            continue
        if maze[x+xx][y+yy] == ".":
            maze[x+xx][y+yy] = maze[x][y]+1
            que.append((x+xx, y+yy))

# print(maze)


'''
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
'''