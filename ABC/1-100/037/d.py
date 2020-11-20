import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[-1 for _ in range(W)] for _ in range(H)]
eight = [(1, 0), (0, 1), (-1, 0), (0, -1)]
mod = 10**9+7

def move(h, w):
    if dp[h][w] != -1:
        return dp[h][w]
    ret = 1

    for x, y in eight:
        nh = h+x
        nw = w+y
        if nh<0 or nh>=H or nw<0 or nw>=W:
            continue
        if A[nh][nw] > A[h][w]:
            ret += move(nh, nw)
    ret %= mod
    dp[h][w] = ret
    return ret

for h in range(H):
    for w in range(W):
        move(h, w)
print(sum([sum(line) for line in dp]) % mod)