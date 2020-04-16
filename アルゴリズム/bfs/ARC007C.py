from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for i in range(R)]

#探索リストQ
Q = deque([[sy-1, sx-1, 0]])

def move(yxc):
    global Q
    y, x, cost = yxc[0], yxc[1], yxc[2]

    #四方のうち、行けるマスに歩数を記録し、座標と歩数をQに追加
    if c[y+1][x]=='.':
        c[y+1][x]=cost+1
        Q.append([y+1,x,cost+1])
    if c[y-1][x]=='.':
        c[y-1][x]=cost+1
        Q.append([y-1,x,cost+1])
    if c[y][x+1]=='.':
        c[y][x+1]=cost+1
        Q.append([y,x+1,cost+1])
    if c[y][x-1]=='.':
        c[y][x-1]=cost+1
        Q.append([y,x-1,cost+1])

c[sy-1][sx-1] = 0
while len(Q) > 0:
    move(Q.popleft())
print(c[gy-1][gx-1])
for i in c:
    print(i)