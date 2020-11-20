'''
スタートを全探索し、移動出来なくなるまで迷路を探索
一番遠い地点までの移動回数を出力
'''

H, W = map(int, input().split())
S = [[i for i in input()] for _ in range(H)]

def dfs(x, y, t, cnt):
    print("x", x, "y", y)
    if S[x][y] == "#" or t[x][y] == True:
        return cnt
    else:
        t[x][y] = True
        cnt += 1
        if H>x+1:
            dfs(x+1, y, t, cnt)
        if x-1>=0:
            dfs(x-1, y, t, cnt)
        if W>y+1:
            dfs(x, y+1, t, cnt)
        if y-1>=0:
            dfs(x, y-1, t, cnt)

ans = 0
print("S", S)
for i in range(H):
    for j in range(W):
        t = [[0 for _ in range(W)] for _ in range(H)]
        print("t", t)
        cnt = 0
        print("dfs", dfs(i, j, t, cnt))
        print(cnt)
        ans = max(ans, cnt)
print(ans)
