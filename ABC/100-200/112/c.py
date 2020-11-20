N = int(input())

H = [list(map(int, input().split())) for _ in range(N)]

for cx in range(101):
    for cy in range(101):
        needH = -1
        for x, y, h in H:
            if h > 0:
                tmp = h+abs(x-cx)+abs(y-cy)
                if needH == -1:
                    needH = tmp
                else:
                    if needH != tmp:
                        needH = -2
                        break
        if needH == -2:
            continue
        f = 1
        for x, y, h in H:
            if h == 0:
                if max(needH-abs(x-cx)-abs(y-cy), 0) != 0:
                    f = 0
                    break
        if f:
            print(cx, cy, needH)
            exit()