N, M = map(int, input().split())
cnt = [1 for _ in range(N)] #市の申請順を管理する
l = []

for i in range(M):
    p, y = map(int, input().split())
    l.append([p, y, i])

l = sorted(l, key=lambda x:x[1])

for i in range(M):
    p = l[i][0] #県
    x = str(cnt[p-1]) #市ができた順位
    cnt[p-1] += 1

    str_p = str(p)
    while len(str_p) != 6:
        str_p = "0" + str_p

    while len(x) != 6:
        x = "0" + x
    
    l[i][0] = str_p
    l[i][1] = x

l = sorted(l, key=lambda x:x[2])

for i, j, _ in l:
    print(i+j)