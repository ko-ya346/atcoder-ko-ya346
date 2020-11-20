H,W = map(int,input().split())
S = [input() for i in range(H)]
 
ans = [[0 for _ in range(W)] for _ in range(H)]
area = [(-1, -1), (-1,  0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        else:
            cnt = 0
            for i, j in area:
                if h+i < 0 or h+i >= H or w+j < 0 or w+j >= W:
                    continue
                else:
                    if S[h+i][w+j] == "#":
                        cnt += 1
            ans[h][w] += cnt

for c in ans:
    cc = [i if i != 0 else "#" for i in c]
    print("".join(list(map(str, cc))))