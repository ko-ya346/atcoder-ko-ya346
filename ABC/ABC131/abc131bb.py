n, l = list(map(int, input().split()))
ans = 0
ans += map
taste = []
abs_l = []
for i in range(n):
    taste.append(l+i)
    abs_l.append(abs(taste[i]))

print(sum(taste)-min(abs_l))