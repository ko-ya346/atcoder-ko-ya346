import heapq

def dijkstra(route_list):
    #ノードの数
    node_num = len(route_list)

    # 未探索ノード
    unsearched_nodes = []
    
    # ノードごとの距離のリスト ->[inf, inf, inf, inf, inf]
    distance = [float("inf")] * node_num 
    # 最短経路でそのノードのひとつ前に到達するノードのリスト
    # previous_nodes = [-1] * node_num 
    # 初期のノードの距離は0
    distance[0] = 0 

    heapq.heappush(unsearched_nodes, (distance[0],0))

    #未探索ノードがなくなるまで繰り返す
    while len(unsearched_nodes) > 0: 
        # まず未探索ノードのうちdistanceが最小のものを選択する
        _, u = heapq.heappop(unsearched_nodes)
        # print("u", u)
        # ターゲットになるノードからのびるエッジのリスト
        target_edge = route_list[u]
        # print("target_edge", target_edge)
        for index, route_dis in enumerate(target_edge):
            #距離が0以外の場合、辺が伸びている
            if route_dis != 0:
                #左辺:すでに記録されているdis、右辺:ターゲットの辺からdisを加えた新しいルート
                if distance[index] > (distance[u] + route_dis):
                    # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                    distance[index] = distance[u] + route_dis
                    heapq.heappush(unsearched_nodes, (distance[index], index))
                    # previous_nodes[index] =  target_min_index 
        # print("dis", distance)
    return distance

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

route = [[0 for _ in range(N)] for _ in range(N)]
reverse_route = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    i, j, c = map(int, input().split())
    route[i-1][j-1] = c
    reverse_route[j-1][i-1] = c
# print("route", route)
# print("r_route", reverse_route)

go_back = [x + y for (x,y) in zip(dijkstra(route), dijkstra(reverse_route))]

ans = 0
# print(go_back)
for i in range(N):
    ans = max((T-go_back[i])*A[i], ans)
print(ans)
