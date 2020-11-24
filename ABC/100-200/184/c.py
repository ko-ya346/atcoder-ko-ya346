r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = r2-r1
c = c2-c1
# 同じマス
if r==c==0:
    ans = 0
# 移動A、B
elif r==c or r==-c:
    ans = 1
# 移動C
elif abs(r)+abs(c)<=3:
    ans = 1
# 移動A, B * 2
elif (r%2==0 and c%2==0) or (r%2 and c%2):
    ans = 2
# 移動C*2
elif abs(r)+abs(c)<=6:
    ans = 2
# 移動A, B + 移動C
elif abs(r+c)<=3 or abs(r-c)<=3:
    ans = 2
else:
    ans = 3
print(ans)