n = int(input())

dan = [int(input()) for _ in range(n)]
seen = []
ans = 0
for i in range(n):
    if i in seen:
        continue
    seen.append(i)
    under = dan[i]
    ans += 1
    for j in range(i+1, n):
        if j in seen:
            continue
        if under >= dan[j]:
            seen.append(j)
            under = dan[j]
print(ans)
