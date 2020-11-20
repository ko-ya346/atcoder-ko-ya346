n = int(input())
a = [input().split() for i in range(n)]

for i in range(n):
    a[i].append(i+1)

a_point = sorted(a, key = lambda x: int(x[1]), reverse = True)

a_name = sorted(a_point, key = lambda x: x[0])

ans = []

for i in a_name:
    print(i[2])