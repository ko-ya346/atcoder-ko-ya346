import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
a = list(map(int, input().split()))
ans = len(a)

num = 1
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        num += 1
    else:
        if num > 2:
            ans += combinations_count(num, 2)
            num = 1
        elif num == 2:
            ans += 1
            num = 1
    # print("i",i, "ans", ans, "num", num)
if num > 2:
    ans += combinations_count(num, 2)
elif num == 2:
    ans += 1
print(ans)