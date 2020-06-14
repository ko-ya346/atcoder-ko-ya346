H, W = map(int, input().split())

a = [list(input()) for _ in range(H)]
dp = [[0 for _ in range(W)] for _ in range(H)]

# print(a)
# print(dp)

dp[0][0] = 1

for i in range(H): #行
    for j in range(W): #列
        if a[i][j] == "#" or (i == H-1 and j == W-1):
            continue

        if i == H-1:
            if a[i][j+1] != "#":
                dp[i][j+1] += dp[i][j]
        elif j == W-1:
            if a[i+1][j] != "#":
                dp[i+1][j] += dp[i][j]
        else:
            if a[i][j+1] != "#":
                dp[i][j+1] += dp[i][j]
            if a[i+1][j] != "#":
                dp[i+1][j] += dp[i][j]

print(dp[-1][-1]%1000000007)