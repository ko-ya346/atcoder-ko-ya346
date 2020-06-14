from collections import deque

N, X, Y = map(int, input().split())
grid = [[float("inf") for _ in range(405)] for _ in range(405)]

#囲いをつける
for i in range(405):
    grid[i][0] = "#"
    grid[0][i] = "#"
    grid[-1][i] = "#"
    grid[i][-1] = "#"

#与えられた障害物をマーク
for _ in range(N):
    x, y = map(int, input().split())
    grid[y+202][x+202] = "#"
grid[202][202] = 0

Q = deque([[202, 202, 0]])

moving = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)]

def move(yx):
    # print(yx)
    global Q
    y, x, cost = yx[0], yx[1], yx[2]
    #四方のうち、行けるマスに歩数を記録し、座標と歩数をQに追加

    for i, j in moving:
        if grid[y+i][x+j] != "#":
            if grid[y+i][x+j] > cost+1:
                grid[y+i][x+j] = cost+1
                Q.append([y+i, x+j, cost+1])


while len(Q):
    move(Q.popleft())

if grid[Y+202][X+202] == float("inf"):
    print(-1)
else:
    print(grid[Y+202][X+202])


# for i in range(195, 205):
    # print(grid[i][197:205])