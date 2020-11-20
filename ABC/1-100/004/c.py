n = int(input())
slide = n//5 % 6
n = n%5
l = list(map(str, range(1, 7)))

l = l[slide:] + l[:slide]
for i in range(n):
    l[i%5], l[i%5+1] = l[i%5+1], l[i%5]
print("".join(l))
