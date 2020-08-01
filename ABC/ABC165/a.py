K = int(input())
a,b=map(int, input().split())

f = 0
for i in range(a, b+1):
    if ((i)%K ==0):
        f = 1

if f:
    print("OK")
else:
    print("NG")