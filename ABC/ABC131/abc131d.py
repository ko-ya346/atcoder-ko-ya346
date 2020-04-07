n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

b = sorted(a, key = lambda x: x[1])

work = 0
flag = 0
for i in range(n):
    work += b[i][0]
    if work > b[i][1]:
        flag = 1
        print("No")
        break

if flag == 0:
    print("Yes")