n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
l = [a, b, c, d, e]
l_m = min(l)

if (n/l_m)%1 == 0:
    print(4+int(n/l_m))
else:
    print(5+int(n/l_m))
