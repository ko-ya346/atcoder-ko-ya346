from itertools import accumulate

n = int(input())
calendar = [i%7==0 or i%7==6 for i in range(366)]
l = list(accumulate([0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))

for _ in range(n):
    month, day = map(int, input().split("/"))
    calendar[l[month-1] + day - 1] += 1


ans = 0
amari = 0
cnt = 0

for i in range(366):
    if calendar[i]>=1:
        amari += calendar[i]-1
        cnt += 1
        ans = max(ans, cnt)
    else:
        if amari:
            cnt += 1
            amari -= 1
            ans = max(ans, cnt)
        else:
            ans = max(ans, cnt)
            cnt = 0

print(ans)