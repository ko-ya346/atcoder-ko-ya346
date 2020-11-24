n, m = map(int, input().split())
b = 0

while b<=n:
    c = (m-2*(n-b))/2
    if c%1==0:
        c = int(c)
        a = n-b-c
        if a>=0 and c>=0:
            print(a, b, c)
            exit()

    b += 1
    m -= 3
print(-1, -1, -1)
