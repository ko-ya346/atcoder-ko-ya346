n = int(input())
s = input()

cnt = []
cnt.append(s[1:].count("E"))
cnt.append(s[:n].count("W"))
for i in range(1, n-1):
    a = s[:i].count("W")+s[i+1:].count("E")
    cnt.append(a)
print(min(cnt))