import copy
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

a_l = []
for i in range(n):
    a_l.append(a[i][0])
a1 = sorted(a_l)
m1 = a1[-1]
m2 = a1[-2] 

for i in a_l:
    if i == m1:
        print(m2)
    else:
        print(m1) 