N = int(input())
H = list(map(int, input().split()))

if N == 1:
    print("Yes")
else:
    f = 1
    for i in range(1, N-1):
        if H[-i-1] <= H[-i]:
            continue
        elif H[-i-1]-1 == H[-i]:
            H[-i-1] -= 1
        else:
            f = 0
            break
    if f:
        print("Yes")
    else:
        print("No")
