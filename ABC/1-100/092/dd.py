# 縦横の制約を満たせない
a, b = map(int, input().split())

ans = [["#" for _ in range(100)] for _ in range(50)]
dot = [["." for _ in range(100)] for _ in range(50)]
ans.extend(dot)

a_cnt = 1
row = 1
col = 1

while a_cnt < a:
    ans[row][col] = "."
    col += 2
    if col >= 100:
        col = 1
        row += 2
    a_cnt += 1

b_cnt = 1
row = 51
col = 1

while b_cnt < b:
    # print(row, col)
    ans[row][col] = "#"
    col += 2
    if col >= 100:
        col = 1
        row += 2
    b_cnt += 1
print(100, 100)
for a in ans:
    print("".join(a))