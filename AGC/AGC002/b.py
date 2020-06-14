N, M = map(int, input().split())

ball = [1 for _ in range(N)]
red = [0 for _ in range(N)]
red[0] = 1

now_red = 0

for i in range(M):
    xx, yy = map(int, input().split())
    x = xx-1
    y = yy-1
    
    ball[x] -= 1
    ball[y] += 1
    
    if red[x]:
        if ball[x] == 0:
            red[x] = 0

        red[y] = 1
        now_red = y
    print("ball", ball)
    print("red", red)
    print("now_red", now_red)

print(sum(red))
    
