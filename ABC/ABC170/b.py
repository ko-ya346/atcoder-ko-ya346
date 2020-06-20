x, y = map(int, input().split())

f = 0
for i in range(x+1):
    # print(x*2+(x-i)*4)
    if i*2+(x-i)*4 == y:
        f = 1

if f:
    print("Yes")
else:
    print("No")