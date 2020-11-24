s = list(input())
K = int(input())

for i in range(len(s)):
    if s[i] == "a":
        continue
    d = ord("z")-ord(s[i]) + 1
    if d <= K:
        s[i] = "a"
        K -= d

x = (ord(s[-1])-ord("a")+K)%26
s[-1] = chr(ord("a")+x)
print("".join(s))