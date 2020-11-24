n, k = map(int, input().split())
s = []
a = 0
for _ in range(n):
    if a == 0:
        a = int(input())
    else:
        na = int(input())
        s.append(str(int(a<na)))
        a = na
ans = 0
s = "".join(s).split("0")
for i in s:
    if len(i)+1>=k:
        ans += len(i)-k+2
print(ans)