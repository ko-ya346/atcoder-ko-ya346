from collections import Counter
n=int(input())
s = dict(Counter(input()))

ans = 0
for k, v in s.items():
    if k=="A":
        ans+=v*4
    elif k=="B":
        ans+=v*3
    elif k=="C":
        ans+=v*2
    elif k=="D":
        ans+=v
print(ans/n)