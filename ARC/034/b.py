n = int(input())
cnt = 0
ans = []
for x in range(max(1, n-153), n+1):
    fx = sum(list(map(int, list(str(x)))))
    if x+fx == n:
        cnt += 1
        ans.append(x)
print(cnt)
if len(ans):
    for i in ans:
        print(i)