H = int(input())
ans = 0

l = []
n = 1

while n <= H:
    l.append(n)
    n *= 2
print(sum(l))