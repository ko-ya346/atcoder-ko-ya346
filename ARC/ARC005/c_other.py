from collections import deque

H, W = map(int, input().split())

B = [[float("inf")]*W for _ in range(H)]

road = []
for i in range(H):
    s = input()
    for j, ss in enumerate(s):
        if ss =="s":
            sy, sx = i,  j
        elif ss == "g":
            gy, gx = i, j
    road.append(list(s))

B[sy][sx] = 0

# print(road)
# print(B)
queue = deque([(sy, sx)])
#黒点をスタート地点とし、上下左右に移動した時の移動距離を記録していく
while queue:
    #qr, qc: 現在地
    qr, qc=queue.popleft()

    #r, c: 次のマス
    for r, c in ((qr+1, qc), (qr-1, qc), (qr, qc+1), (qr, qc-1)):
        if r >= 0 and r <= H-1 and c >= 0 and c <= W-1:
            # print(r, c)
            wall = (road[r][c] == "#")
            d2 = B[qr][qc] + wall
            if B[r][c] > d2:
                B[r][c] = d2
                if wall:
                    queue.append((r, c))
                else:
                    queue.appendleft((r, c))
    if B[gy][gx] <= 2:
        print("YES")
        exit() 
# print(B)
print("NO")
# print(max([max(b) for b in B]))
