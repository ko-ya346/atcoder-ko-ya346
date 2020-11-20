N, M, X, Y = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if X+1>Y:
    print("War")
else:
    if (max(x)+1) > min(y):
        print("War")
    else:
        if X +1 > min(y) and Y > max(x):
            print("No War")
        else:
            print("No War")