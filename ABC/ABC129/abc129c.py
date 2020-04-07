n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(m)]

badstep = set()
for i in a:
    badstep.add(i[0])
print(badstep)
ans = []
step = 0
flag1 = 0
flag2 = 0

for i in range(n-1):
    pattern = 0
    step += 1
    if step in badstep:
        flag1 = 1
    else:
        flag1 = 0
        pattern += 1
    if step == n:
        break
    step1 = step
    step1 += 1
    if step1 in badstep:
        flag2 = 1
    else:
        flag2 = 0
        pattern += 1
    if flag1 == flag2 == 1:
        break
    
    ans.append(pattern)

l = 1
for i in ans:
    l = l*i
print(l%1000000007)