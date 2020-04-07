n = int(input())
east = int(input())*0.01
west = int(input())*0.01
south = int(input())*0.01
north = int(input())*0.01
prob = [east, west, south, north]

grid = [[False for i in range(100)] for j in range(100)]
vx = [1,-1,0,0]
vy = [0,0,1,-1]

def dfs(x, y, n):
    if grid[x][y]:
        return 0
    if n == 0:
        return 1
    grid[x][y] = True
    ret = 0
    for i in range(4):
        ret += dfs(x+vx[i], y+vy[i], n-1)*prob[i]
    grid[x][y] = False
    return ret

print(dfs(50, 50, n))