# 1頂点消して、最短距離を出す
# N回O(N^2)なのでO(N^3)
from scipy.sparse import *
import numpy as np
N,M = map(int,input().split())
UVL = [[int(x) for x in input().split()] for _ in range(M)]
U,V,L = zip(*UVL)
graph = csr_matrix((L,(U,V)), (N+1,N+1), dtype=np.float64)

answer = np.inf
# u < v が保証されている
for u,v,weight in UVL:
  if u != 1:
    continue
  # 消してみる
  graph[u,v] = np.inf
  dist = csgraph.dijkstra(graph, indices = 1, directed = False)
  x = dist[v] + weight
  if answer > x:
    answer = x
  # 戻す
  graph[u,v] = weight

answer = int(answer) if answer != np.inf else -1
print(answer)
