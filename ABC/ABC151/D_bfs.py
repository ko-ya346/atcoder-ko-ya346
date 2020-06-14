from collections import deque

H,W = map(int, input().split())
s = ["#"*(W+2)]+["#"+input()+"#" for i in range(H)]+["#"*(W+2)]

def bfs(sh,sw):
  if s[sh][sw] == "#":
    return 0
  queue = deque([(sh,sw)]) #スタート地点をdequeに入れる
  dist = [[-1] * (W+1) for i in range(H+1)] #距離をメモするリストを作成
  dist[sh][sw] = 0 #スタート地点の距離を0にする
  while queue:
    h,w = queue.popleft() #queueの左から位置情報を取り出す
    d = dist[h][w] #現在のマスの数字を保持(移動距離)
    # print("dist", dist)
    for i in [h-1,h+1]: #x軸に前後する
      if s[i][w] == "." and dist[i][w] == -1: #行ける、かつ未踏破のマス
        dist[i][w] = d + 1 #移動距離をメモ
        queue.append((i,w)) #移動先のマスをqueueに格納
    for j in [w-1,w+1]: #y軸を行ったり来たり
      if s[h][j] == "." and dist[h][j] == -1:
        dist[h][j] = d + 1
        queue.append((h,j))
          
  max_dist = 0
  for i in dist:
    max_dist = max(max_dist,max(i)) #移動距離が多いマスを抽出
  return max_dist
      

ans = 0          
for i in range(1,H+1):
  for j in range(1,W+1):
    now = bfs(i,j)
    ans = max(ans, now)
print(ans)
