#最長共通部分列
# https://qiita.com/_rdtr/items/c49aa20f8d48fbea8bd2

#比較する文字列
s1 = input()
s2 = input()

table = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

#0行目を埋める
f = 0
for i in range(len(s2)):
    if f or s2[i] == s1[0]:
        table[i][0] = 1
        f = 1

#0列目を埋める
f = 0
for i in range(len(s1)):
    if f or s2[0] == s1[i]:
        table[0][i] = 1
        f = 1


for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        #上マスと左マスは考慮済みなので、左上から遷移する
        if s2[i] == s1[j]:
            table[i][j] += table[i-1][j-1]+1
        else:
            if i == 0 or j == 0:
                continue
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

# for col in table:
#     print(col)

#最長文字列を求める
lcs_str = ""
i, j = len(s2)-1, len(s1)-1

while i >= 0 and j >= 0:
    # print("i", i, "j", j)
    if s2[i] == s1[j]:
        # print("c")
        lcs_str += s2[i] #or s2[j-1]
        i -= 1
        j -= 1
    else:
        if j == 0:
            i -= 1
        elif i == 0:
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                i -= 1
            else:
                j -= 1
print(lcs_str[::-1])
