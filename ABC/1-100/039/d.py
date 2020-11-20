H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
origin = [["." for _ in range(W)] for _ in range(H)]
eight = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def judge(h, w):
    f = 1
    for x, y in eight:
        nh = h+x
        nw = w+y
        if nh<0 or nh>=H or nw<0 or nw>=W:
            continue
        if S[nh][nw] == ".":
            f = 0
            break
    if f:
        return "#"
    else:
        return "."

res = [["." for _ in range(W)] for _ in range(H)]

def restration(h, w):
    if origin[h][w]=="#":
        res[h][w] = "#"
        for x, y in eight:
            nh = h+x
            nw = w+y
            if nh<0 or nh>=H or nw<0 or nw>=W:
                continue
            res[nh][nw] = "#"

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            origin[h][w] = judge(h, w)

for h in range(H):
    for w in range(W):
        restration(h, w)

if S==res:
    print("possible")
    for i in range(H):
        print("".join(origin[i]))
else:
    print("impossible")