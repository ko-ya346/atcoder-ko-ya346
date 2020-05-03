
s = input()[::-1]

ans=0

#判定する数字
u=0

#桁
d=1

#余りのリストを格納
l=[0]*2019
l[0]=1

for i in map(int,s):
    u=(u+(i*d)%2019)%2019
    l[u]+=1
    d=d*10%2019
for i in l:
    ans+=i*(i-1)//2
print(ans)

'''
from collections import Counter

S = input()
N = len(S)

s = [0 for _ in range(N)]

num = ""
for i in range(N-1, -1, -1):
    num = S[i] + num <-　たぶんここが遅い
    s[i] += int(num)%2019

ans = 0
# print(Counter(a))
for key, val in Counter(s).items():
    if key == 0:
        ans += val
    if val >= 2:
        ans += val*(val-1)//2
print(ans)
'''