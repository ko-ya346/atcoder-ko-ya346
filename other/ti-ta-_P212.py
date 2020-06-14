# donations = list(map(int, input().split()))
def f():
    dx = [1,1,1,0,-1,-1,-1,0,2,1,-1,-2,-2,-1,1,2]
    dy = [1,0,-1,-1,-1,0,1,1,-1,-2,-2,-1,1,2,2,1]

    size = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    numMove = int(input())

    sx = start[0]
    sy = start[1]
    ex = end[0]
    ey = end[1]
    ways = [[[0 for _ in range(55)] for _ in range(100)] for _ in range(100)]
    ways[sy][sx][0] = 1

    for i in range(1, numMove+1):
        for x in range(size):
            for y in range(size):
                for j in range(16):
                    nx = x+dx[j]
                    ny = y+dy[j]
                    if (nx<0 or ny<0 or nx>=size or ny>=size):
                        continue
                    ways[ny][nx][i] += ways[y][x][i-1]
    # print(ways)
    return ways[ey][ex][numMove]

print(f())

'''
3
0 0
1 2
1

100
0 0
0 99
50
'''