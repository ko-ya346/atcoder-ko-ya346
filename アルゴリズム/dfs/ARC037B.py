
#このdfsでは判定がfor文の外にあるので、先へ進むことができない！！
def dfs(n):
    global flag
    global last

    if n in last :
        return
    elif judge[n]:
        flag = 0
        return 
    judge[n]= True
    
    last.append(n)
    print("n",n)
    for i in l[n]:
        dfs(l[i-1][0]-1)

N, M = list(map(int, input().split()))

l = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    l[a-1].append(b)
    l[b-1].append(a)

judge = [False for _ in range(N)]

ans = 0

for k in range(N):
    print("judge", judge, "k", k)
    if judge[k] == False:
        flag = 1
        last = []
        dfs(k)
        print("flag", flag)
        if flag:
            ans += 1

print(ans)
print(l)