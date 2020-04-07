n = int(input())
a = [input().split() for i in range(n)]

a_s = sorted(a)
count = 0
iiii = 0

for i in range(len(a)-1):
    ii = int(a[i][0])
    iii = int(a[i+1][0])
    if iii != ii:
        iiii = i
        if (ii-iiii)%2 == 1:
            count += 1

print(count)
