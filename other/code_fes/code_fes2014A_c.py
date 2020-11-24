A, B = map(int, input().split())

A -= 1
b = B//4-B//100+B//400
a = A//4-A//100+A//400

print(b-a)

ans = 0
for i in range(A, B+1):
    if i%400==0:
        ans += 1
    elif i%100==0:
        continue
    elif i%4==0:
        ans += 1
print(ans)
