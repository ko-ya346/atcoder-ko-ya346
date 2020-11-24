from datetime import *

# 土日はFalse
c = [0 < i%7 < 6 for i in range(732)]
print(c)

for _ in range(int(input())):
    i = (date(2012, *map(int, input().split("/")))-date(2012, 1, 1)).days
    while c[i] < 1:
        # iが休みの場合、平日まで進む
        i += 1
    # 休みに認定
    c[i] = 0

a = t = 0
for i in c[:366]:
    if i:
        t = 0
    else:
        t += 1
    a = max(a, t)
print(a)