n = int(input())
a = [input().split() for i in range(n)]

for i in range(n):
    a[i].append(i+1)

b = sorted(a, key = lambda x:int(x[1]), reverse = True)
c = sorted(b, key = lambda x:x[0])

for i in c:
    print(i[2])