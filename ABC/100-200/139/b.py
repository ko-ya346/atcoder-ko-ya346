a, b = map(int, input().split())
if b == 1:
    print(0)
elif a >= b:
    print(1)
else:

    print(-(-(b-a)//(a-1))+1)