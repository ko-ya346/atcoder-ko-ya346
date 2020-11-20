N = int(input())
a = list(map(int, input().split()))

ans = float("inf")

for i in range(-101,102):
    cost = 0
    for j in a:
        cost += (i-j)**2
    ans = min(ans, cost)
print(ans)