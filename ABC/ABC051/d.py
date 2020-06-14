from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np

n,m,k = map(int,input().split())
abc = [list(map(int,input().split())) for _ in range(m)]
 
row,col,data = zip(*abc)
# print("abc", abc)
# print(row,col,data)

L = csr_matrix((data, (row,col)), shape=(n+1,n+1))
# print("L", L)

#directed=False:無向グラフ、return_predecessors=True:
#返り値1は各点までの最短距離、返り値は最短経路（return_predecessors=Trueが必要）
_,path = dijkstra(L,directed = False, return_predecessors = True)
print("path", path)

#条件に合致するindexを返す（1つめ：行、２つめ：列）
s, e = np.where(path>0)
print(s, e)
print(np.vstack([path[s,e],e]))
path_use = set(map(tuple,np.vstack([path[s,e],e]).T))
 
# print( m - len(path_use)//2)

def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])

def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    print(pred_row)
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
        print(i)
    if i < 0:
        return []
    path.append(i)
    return path[::-1]
# print(get_path(3, 2, path))