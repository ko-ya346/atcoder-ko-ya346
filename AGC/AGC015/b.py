s = input()

ans = len(s)*(len(s)-1)
for i in range(len(s)):
    if s[i] == "U":
        ans += i
    else:
        ans += len(s)-i-1
print(ans)