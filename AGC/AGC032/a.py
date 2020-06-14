N = int(input())
b = list(map(int, input().split()))

ans = []

for i in range(N):
    pop = -1
    for j, v in enumerate(b):
        if j+1 == v:
            pop = j
    if pop == -1:
        print(-1)
        exit()
    ans.append(b.pop(pop))
for i in ans[::-1]:
    print(i)