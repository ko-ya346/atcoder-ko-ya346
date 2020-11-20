h, w = map(int, input().split())

grid = []
for _ in range(h):
    row = input()
    grid.append(row)

dp = [[0 for _ in range(w)] for _ in range(h)]

# 一気に移動する場合
for i in range(h):
    cnt = 0
    for j in range(w):
        if grid[i][j] == ".":
            dp[i][j] += cnt
            cnt += 1
        else:
            cnt = 0

for j in range(w):
    cnt = 0
    for i in range(h):
        if grid[i][j] == ".":
            dp[i][j] += cnt
            cnt += 1
        else:
            cnt = 0


# # 行方向の累積和
# for i in range(h):
#     flag = 0
#     for j in range(w-1):
#         if grid[i][j] == ".":
#             flag = 1
#         else:
#             flag = 0
#         if grid[i][j+1] == ".":
#             dp[i][j+1] += dp[i][j]+flag

# # 列方向の累積和
# for j in range(w):
#     flag = 0
#     for i in range(h-1):
#         if grid[i][j] == ".":
#             flag = 1
#         else:
#             flag = 0
#         if grid[i+1][j] == ".":
#             dp[i+1][j] += dp[i][j]+flag


print(dp)
print(grid)