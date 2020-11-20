N = int(input())

c = [int(input()) for _ in range(N)]
cnt = 0
num = c[0]
for i in range(N-1):
    if num > c[i+1]:
        cnt += 1
        num = c[i]
    else:
        num = c[i+1]
print(cnt)