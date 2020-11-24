N = int(input())

ans = 0
for i in range(49999):
    if int(i*1.08) == N:
        ans = i

if ans:
    print(ans)
else:
    print(":(")