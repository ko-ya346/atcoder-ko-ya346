N, D, K = map(int, input().split())
day = [list(map(int, input().split())) for _ in range(D)]

for k in range(K):
    s, t = map(int, input().split())
    flag = 0
    if s > t:
        flag = 1
    for i, (d1, d2) in enumerate(day):
        if (d1<=s<=d2):
            if (d1<=t<=d2):
                print(i+1)
                break
            else:
                if flag:
                    s = d1
                else:
                    s = d2



