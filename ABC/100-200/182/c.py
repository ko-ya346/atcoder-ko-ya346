N = [int(i)%3 for i in input()]

SUM = sum(N)%3
if SUM%3 == 0:
    print(0)
elif SUM%3 == 1:
    if len(N) >= 2 and 1 in N:
        print(1)
    elif len(N) >= 3 and N.count(2) >= 2:
        print(2)
    else:
        print(-1)
else:
    if len(N) >= 2 and 2 in N:
        print(1)
    elif len(N) >= 3 and N.count(1) >= 2:
        print(2)
    else:
        print(-1)