n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
overpower = 0
for i in range(n):
    if a[i] >= overpower:
        ans += overpower
        enemy = a[i] - overpower
    else:
        ans += a[i]
        enemy = 0
    overpower = 0
    
    if enemy >= b[i]:
        ans += b[i]
    else:
        ans += enemy
        overpower = b[i]-enemy

if a[-1]>=overpower:
    print(ans+overpower)
else:
    print(ans+a[-1])   
