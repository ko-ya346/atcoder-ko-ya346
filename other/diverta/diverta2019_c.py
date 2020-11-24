N = int(input())

ab = 0
x = 0
y = 0
z = 0

for _ in range(N):
    s = input()
    ab += s.count("AB")
    if (s[-1] == "A" and s[0] == "B"):
        z += 1
    elif (s[-1] == "A"):
        x += 1
    elif (s[0] == "B"):
        y += 1

if (not x and not y) and z:
    print(ab + z-1)
else:
    print(ab + min(x+z, y+z))