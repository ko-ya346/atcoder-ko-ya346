from math import factorial

N, K = map(int, input().split())
town = []

for _ in range(N):
    t = list(map(int, input().split()))
    town.append(t)

ans = 0
def dfs(now, k, cnt):
    global ans
    if cnt == N-1:
        if k + town[now][0] == K:
            ans += 1
        return
    searched[now] = True

    # print(now, k, cnt)
    for i in range(N):
        if now == i:
            continue
        if searched[i]:
            continue

        dfs(i, k + town[now][i], cnt + 1)
    searched[now] = False

searched = [False for _ in range(N)]
dfs(0, 0, 0)
print(ans)