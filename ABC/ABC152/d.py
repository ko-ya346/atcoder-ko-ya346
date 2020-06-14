n = int(input())
ct = [[0] * 10 for _ in range(10)]
print(ct)

for i in range(n + 1):
    i = str(i)
    ct[int(i[0])][int(i[-1])] += 1
print(ct)
ans = 0
for i in range(1, 10):
    ans += ct[i][i] ** 2
for i in range(1, 10):
    for j in range(i + 1, 10):
        ans += ct[i][j] * ct[j][i] * 2
print(ans)