k = int(input())

num = 7
ans = 0
for i in range(k+1):
    if i==0:
        num %= k
    else:
        num = (num*10 + 7)%k
    ans += 1
    if num == 0:
        print(ans)
        exit()
print(-1)