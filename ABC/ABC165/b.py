X = int(input())

n = 100
cnt = 0
while n < X:
    # print(n)
    n *= 100
    # print(n)
    n += int(n/100)
    # print(n)
    n //= 100
    # print(n)
    cnt += 1

print(cnt)
