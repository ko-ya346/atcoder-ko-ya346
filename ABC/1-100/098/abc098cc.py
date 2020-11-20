n = int(input())
s = input()

a = 0
cnt = []
for i in range(n):
    if s[i] == "W":
        a += 1
    cnt.append(a)

ans = []
for i in range(n):
    ans.append()