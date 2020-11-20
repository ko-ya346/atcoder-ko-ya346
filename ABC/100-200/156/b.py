n, k = map(int, input().split())

num = 1

while True:
    if n < k:
        break
    num += 1
    n //= k
print(num)