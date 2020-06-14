N = int(input())
a = list(map(int, input().split()))

right = sum(a)
left = 0
ans = float("inf")

for i in a:
    left += i
    right -= i
    # print(right-left)
    ans = min(ans, abs(right-left))
print(ans)