# https://qiita.com/shizuma/items/e08a76ab26073b21c207
import math

route_list = [[0, 50, 80, 0, 0], [0, 0, 20, 15, 0 ], [0, 0, 0, 10, 15], [0, 0, 0, 0, 30], [0, 0, 0, 0, 0]] # 初期のノード間の距離のリスト

#ノードの数
node_num = len(route_list)

# 未探索ノード ->[0, 1, 2, 3, 4]
unsearched_nodes = list(range(node_num)) 
# ノードごとの距離のリスト ->[inf, inf, inf, inf, inf]
distance = [math.inf] * node_num 
# 最短経路でそのノードのひとつ前に到達するノードのリスト
previous_nodes = [-1] * node_num 
# 初期のノードの距離は0
distance[0] = 0 

#未探索ノードがなくなるまで繰り返す
while(len(unsearched_nodes) != 0): 
    # まず未探索ノードのうちdistanceが最小のものを選択する

    # 最小のdistanceの入れ物。初期値は inf に設定。
    posible_min_distance = math.inf 
    # 未探索のノードに対応するdistanceを列挙
    for node_index in unsearched_nodes: 
        # より小さい値が見つかれば更新
        if posible_min_distance > distance[node_index]: 
            posible_min_distance = distance[node_index] 
    # 未探索ノードのうちで最小のindex番号を取得
    target_min_index = distance.index(posible_min_distance)
    # ここで探索するので未探索リストから除去
    unsearched_nodes.remove(target_min_index) 

    # ターゲットになるノードからのびるエッジのリスト
    target_edge = route_list[target_min_index]
    for index, route_dis in enumerate(target_edge):
        #距離が0以外の場合、辺が伸びている
        if route_dis != 0:
            #左辺:すでに記録されているdis、右辺:ターゲットの辺からdisを加えた新しいルート
            if distance[index] > (distance[target_min_index] + route_dis):
                # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                distance[index] = distance[target_min_index] + route_dis
                #　ひとつ前に到達するノードのリストも更新 
                previous_nodes[index] =  target_min_index 

print("-----経路-----")
previous_node = node_num - 1
while previous_node != -1:
    if previous_node !=0:
        print(str(previous_node + 1) + " <- ", end='')
    else:
        print(str(previous_node + 1))
    previous_node = previous_nodes[previous_node]

print("-----距離-----")
print(distance)
print(distance[node_num - 1])