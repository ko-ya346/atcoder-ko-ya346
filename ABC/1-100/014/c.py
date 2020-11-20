n = int(input())

num = 10**6
enogu = [0] * (num+1)

for _ in range(n):
    a, b = map(int, input().split())
    enogu[a] += 1
    if b+1 <= num:
        enogu[b+1] -= 1

for i in range(num):
    enogu[i+1] += enogu[i]

print(max(enogu))
# print(enogu[:8])