n, l = list(map(int, input().split()))

taste = []
abs_l = {}
for i in range(n):
    taste.append(l+i)
    abs_l[i] = abs(taste[i])

a_min = min(abs_l, key = abs_l.get)
print(sum(taste)-taste[a_min])