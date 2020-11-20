from math import degrees, cos,sqrt ,radians, pi

A, B, H, M = map(int, input().split())

if H == 6 and M == 0:
    print(A+B)
    exit()


kaku = abs(6*M-(0.5*M+H*30))/180*pi
# if kaku > 180:
#     kaku = 360 - kaku
# print(kaku)
# if kaku > 90:
#     kaku = 180-kaku
# print(kaku)
# print(cos(radians(kaku)))
print(sqrt(A**2 + B**2 -2*A*B*cos(kaku)))

# print(-A*B*cos(kaku))
# 3 4 7 0