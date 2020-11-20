import sys #追加
sys.setrecursionlimit(500*500)

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

time = 0
cnt = 0
ans = 0
ai = -1
bi = -1

def dfs(time, cnt):
    global ans, ai, bi
    # print(time)
    if time > K:
        # print(cnt)
        ans = max(ans, cnt-1)
        return
    if ai <= N-2:
        ai += 1
        dfs(time+A[ai], cnt+1)
    if bi+1 <= M-2:
        bi += 1
        dfs(time+B[bi]+1, cnt+1)

if sum(A)+sum(B)<=K:
    print(N+M)
else:
    dfs(0, 0)
    print(ans)