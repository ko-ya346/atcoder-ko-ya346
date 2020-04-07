n = int(input())
f = [input().split() for i in range(n)]
l = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    a = f[i][0]
    for j in range(n):
        if a[j] == "Y":
            l[i][j] = 1

ans = []
for i in l:
    for j in range(n):
        if i[j] == 1:
            ans.append(sum(i)+sum(l[j])-1)

if max(ans) <= 1:
    print(1)
else:
    print(max(ans)-1)