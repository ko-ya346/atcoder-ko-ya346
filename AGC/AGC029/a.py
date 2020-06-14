S = input()

cnt = 0
ans = 0

for i, s in enumerate(S[::-1]):
    if s =="B":
        ans += i - cnt
        cnt += 1
print(ans)