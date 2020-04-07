a = list(map(int, input().split()))
a.sort()
print(abs(a[2]-a[1])+abs(a[1]-a[0]))