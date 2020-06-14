h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

dp = [[h*w for i in range(w+1)] for j in range(h+1)]

dp[0][1] = 0
dp[1][0] = 0

for i in range(h):
    for j in range(w):
        # print("i", i, "j", j, "s[i][j]", s[i][j])
        # print(s[i][j] == '#' and (i == 0 or s[i-1][j] == '.'))
        
        #前の道が（"."またはグリッド外）かつ現在地が#の場合に1を加える
        #前の道が"#"であればまとめて変換できるので何も加えない
        dp[i+1][j+1] = min(
            dp[i][j+1] + (s[i][j] == '#' and (i == 0 or s[i-1][j] == '.')),
            dp[i+1][j] + (s[i][j] == '#' and (j == 0 or s[i][j-1] == '.'))
        )

print(dp[-1][-1])
