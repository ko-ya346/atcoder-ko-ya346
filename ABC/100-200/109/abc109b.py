N = int(input())
a = [input() for i in range(N)]

if len(a) != len(set(a)):
    print("No")
else:
    for i in range(N-1):
        aa = a[i]
        bb = a[i+1]
        if aa[-1] != bb[0]:
            print("No")
            break
    else:
        print("Yes")