n = int(input())
A = list(map(int, input().split()))

max_cnt = 0
ans = 0
for i in range(2, max(A) + 1):
    cnt = 0
    for a in A:
        if a%i == 0:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        ans = i
print(ans)
