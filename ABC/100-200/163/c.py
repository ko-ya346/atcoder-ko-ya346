N = int(input())

a = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i in a:
    ans[i-1] += 1

for n in ans:
    print(n)