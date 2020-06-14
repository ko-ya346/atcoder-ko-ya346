N = int(input())
a  =list(map(int, input().split()))
a.sort()

ans1 = a[-1]
ans2 = 0

for i in a:
    if abs(ans1/2-ans2) > abs(ans1/2-i):
        ans2 = i
print(ans1, ans2)