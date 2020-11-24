N, A, B = map(int, input().split())
S = input()

su = A+B
a = 0
b = 0


for i in range(N):
    f = 0
    if S[i] == "a":
        if su > a + b:
            f = 1
            a += 1
    elif S[i] == "b":
        if su > a+b and B > b:
            f = 1
            b += 1
    if f:
        print("Yes")
    else:
        print("No")