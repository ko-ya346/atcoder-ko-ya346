#無向グラフをdfsで全探索し、同じ場所に行きつく（閉路）場合にFalseを返す
def dfs(n,last):
    global flag

    judge[n]= True
    for i in l[n]:
        #直前に訪れた場所をメモし、誤判定しないようにする
        if i != last:
            if judge[i]:
                flag = 0
            else:
                dfs(i, n)

N, M = list(map(int, input().split()))

l = [[] for _ in range(N)]

#入力から無向グラフのリストを作成する
for _ in range(M):
    a, b = map(int, input().split())
    #リストに追加するときに数値を-1すると分かりやすい
    l[a-1].append(b-1)
    l[b-1].append(a-1)

#訪れたかどうかの判定用
judge = [False for _ in range(N)]

ans = 0


for k in range(N):
    #まだ訪れていない地点をスタートとして全探索する
    if judge[k] == False:
        flag = 1
        dfs(k, -1)
        if flag:
            ans += 1

print(ans)