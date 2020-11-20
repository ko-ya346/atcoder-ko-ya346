a, b, c, d = map(int, input().split())

if c%b:
    aoki = c//b + 1
else:
    aoki = c//b

if a%d:
    ta = a//d + 1
else:
    ta = a//d

if aoki > ta:
    print("No")
else:
    print("Yes")