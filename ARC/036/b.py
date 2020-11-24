n = int(input())
h = [int(input()) for _ in range(n)]
M = [0 for _ in range(n-1)]
for i in range(n-1):
    if h[i]<h[i+1]:
        M[i] = 1
ans = 0

flag = 0
cnt = 0
for r, m in enumerate(M):
    if m==1:
        if flag == 0:
            ans = max(ans, cnt)
            cnt = 0
        flag = 1
    else:
        if flag:
            flag = 0
    cnt += 1
    
    

print(max(ans, cnt)+1)