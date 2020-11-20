N = int(input())
s = sorted([int(input()) for _ in range(N)])

l10 = []
l = []

for i in s:
    if i%10:
        l.append(i)
    else:
        l10.append(i)

ss = l + l10
# print(s)
# print(ss)
if sum(ss)%10 == 0:
    while sum(ss)%10 == 0:
        # print(s)
        if ss:
            ss.pop(0)
        else:
            break
    ans = sum(ss)
else:
    ans = sum(ss)
print(ans)
