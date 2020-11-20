s = input()
t = input()

alf = "abcdefghijklmnopqrstuvwxyz"
dic = {}
for a in alf:
    lst = []
    for i, ss in enumerate(s):
        if a == ss:
            lst.append(i+1)
    if len(lst)==0:
        lst.append(0)
    dic[a] = lst

n = len(s)
cnt = 0
before = -1

for tt in t:
    flag = 1

    lst = dic[tt]
    for l in lst:
        # print("l", l)
        if l == 0:
            print(-1)
            exit()
        if before < l:
            flag = 0
            break
    # print("cnt", cnt)
    before = l
    if flag:
        cnt += 1
    # print("before", before)
print(cnt*n + l)

