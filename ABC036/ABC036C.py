def dfs(x, y):
    global ans
    if x == W and y == H:
        ans += 1
    elif x == W:
        dfs(x, y+1)
    elif y == H:
        dfs(x+1, y)
    else:
        dfs(x+1, y)
        dfs(x, y+1)

W, H = list(map(int, input().split()))
ans = 0
dfs(1,1)
print(ans%1000000007)