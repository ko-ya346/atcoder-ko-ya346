S = input().replace("25", "X") + "."
niko = []

cnt = 0
for s in S:
    if s=="X":
        cnt += 1
    else:
        if cnt:
            niko.append(cnt)
            cnt = 0

l = []
cnt = 0
for i in range(1, 100001):
    l.append(cnt)
    cnt += i

ans = 0
for ni in niko:
    ans += l[ni]
print(ans)