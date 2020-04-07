s = input()
i = len(s)
cnt = 0
for j in range(len(s)):
    print(s[j],s[i-j-1])
    if i-j-1 < len(s) and (s[j] != s[i-j-1]):
        cnt += 1
print(cnt//2+i)