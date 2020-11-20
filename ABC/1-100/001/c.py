from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
deg, dis = map(int, input().split())

deg *= 10
dis = int(dis/6*10)
# print(dis)

if len(str(dis)) == 1:
    dis = 0
elif dis%10 >= 5:
    dis = int(str(dis+10)[:-1])
else:
    dis = int(str(dis)[:-1])
# print(dis)

if 1125 <= deg < 3375:
    direction = "NNE"
elif 3375 <= deg < 5625:
    direction = "NE"
elif 5625 <= deg < 7875:
    direction = "ENE"
elif 7875 <= deg < 10125:
    direction = "E"
elif 10125 <= deg < 12375:
    direction = "ESE"
elif 12375 <= deg < 14625:
    direction = "SE"
elif 14625 <= deg < 16875:
    direction = "SSE"
elif 16875 <= deg < 19125:
    direction = "S"
elif 19125 <= deg < 21375:
    direction = "SSW"
elif 21375 <= deg < 23625:
    direction = "SW"
elif 23625 <= deg < 25875:
    direction = "WSW"
elif 25875 <= deg < 28125:
    direction = "W"
elif 28125 <= deg < 30375:
    direction = "WNW"
elif 30375 <= deg < 32625:
    direction = "NW"
elif 32625 <= deg < 34875:
    direction = "NNW"
else:
    direction = "N"

if dis <= 2 :
    speed = 0
elif dis <= 15:
    speed = 1
elif dis <= 33:
    speed = 2
elif dis <= 54:
    speed = 3
elif dis <= 79:
    speed = 4
elif dis <= 107:
    speed = 5
elif dis <= 138:
    speed = 6
elif dis <= 171:
    speed = 7
elif dis <= 207:
    speed = 8
elif dis <= 244:
    speed = 9
elif dis <= 284:
    speed = 10
elif dis <= 326:
    speed = 11
else:
    speed = 12

if speed == 0:
    direction = "C"
print(direction, speed)
