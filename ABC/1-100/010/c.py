import math
txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
dis = T * V
# print(dis)

flag = 0
for _ in range(n):
    x, y = map(int, input().split())
    sg = math.sqrt((y-tya)**2+(x-txa)**2)
    gg = math.sqrt((y-tyb)**2+(x-txb)**2)
    # print(f"sggg: {sg+gg}")
    if sg+gg <= dis:
        flag = 1
if flag:
    print("YES")
else:
    print("NO")