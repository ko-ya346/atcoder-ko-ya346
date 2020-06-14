N = int(input())
a = list(map(int, input().split()))

ans = 0
for i, v in enumerate(a):
    if i == a[v-1]-1:
        ans += 1
print(ans)