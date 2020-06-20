#未訪問をset管理、訪問済を訪れない　ことで時間内に計算が完了する
H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

C = [input() for _ in range(H)]
#訪問済チェック
T = [[-1 for _ in range(W)] for _ in range(H)]
T[x1-1][y1-1] = 0

#未訪問をsetで管理
que = set([(x1-1, y1-1)])
step = 1

while len(que) > 0:
    que_next = set()
    for q in que:
        x, y = q[0], q[1]

        #左に進む
        for i in range(1, K+1):
            #マスからはみ出す
            if x-i<0:
                break
            #障害物もしくは到達済
            if C[x-i][y]=='@' or T[x-i][y]==1:
                break
            #一度に進めるマスをnextに追加
            que_next.add((x-i,y))
        #右に進む
        for i in range(1,K+1):
            if x+i>H-1:
                break
            if C[x+i][y]=='@' or T[x+i][y]==1:
                break
            que_next.add((x+i,y))
        #下
        for i in range(1,K+1):
            if y-i<0:
                break
            if C[x][y-i]=='@' or T[x][y-i]==1:
                break
            que_next.add((x,y-i))
        #上
        for i in range(1,K+1):
            if y+i>W-1:
                break
            if C[x][y+i]=='@' or T[x][y+i]==1:
                break
            que_next.add((x,y+i))
    que = que_next
    for q in que:
        #ゴールなら終了
        if q[0] == x2-1 and q[1] == y2-1:
            print(step)
            exit()
        T[q[0]][q[1]] = 1
    step += 1

print(-1)