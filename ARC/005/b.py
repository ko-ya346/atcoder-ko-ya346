y, x, W = input().split()
C = [list(input()) for _ in range(9)]
x = int(x)-1
y = int(y)-1

ans = C[x][y]
all_move = {"R": (0, 1), "L": (0, -1), "U": (-1, 0),
    "D": (1, 0), "RU": (-1, 1), "RD": (1, 1),
    "LU": (-1, -1), "LD": (1, -1)}
nx, ny = all_move[W]

for _ in range(3):
    xflag = 0
    yflag = 0
    if x + nx < 0 or x + nx >= 9:
        xflag = 1
    if y + ny < 0 or y + ny >=9:
        yflag = 1
    
    if xflag:
        nx *= -1
    if yflag:
        ny *= -1
    x += nx
    y += ny
    ans += C[x][y]
            

print(ans)