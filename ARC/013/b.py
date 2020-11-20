N = int(input())

a, b, c = 0,0,0

for _ in range(N):
    m = sorted(list(map(int, input().split())))
    a = max(a, m[0])
    b = max(b, m[1])
    c = max(c, m[2])
print(a*b*c)