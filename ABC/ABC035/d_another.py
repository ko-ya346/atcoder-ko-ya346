#!/usr/bin/env python3
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix


def solve(N: int, M: int, T: int, A: "List[int]", abc):

	a = abc[:, 0]
	b = abc[:, 1]
	c = abc[:, 2]

	#疎行列に圧縮
	edge = csr_matrix((c, (a, b)), (N+1, N+1))
	#indices:スタート地点
	#https://juppy.hatenablog.com/entry/2019/06/04/scipy%E3%81%AEFloyd-Warshall%E3%81%A8Dijkstra%E3%81%AE%E3%81%99%E3%81%99%E3%82%81_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder_1
	#詳しくは
	forward_dist = dijkstra(edge, indices=1)
	# print(forward_dist)
	edge2 = csr_matrix((c, (b, a)), (N+1, N+1))
	back_dist = dijkstra(edge2, indices=1)
	# print(back_dist)

	# N <= 10**5, M <= 10**5, T <= 10**9
	# 行きの道のり、帰りの道のりをダイクストラで求める O(NlogN)
	# 帰ってこられない節点を除く
	# コストを差し引いて最も稼げるところを求める O(N)
	# print((forward_dist + back_dist))
	cost = (A*(T-(forward_dist + back_dist)[1:])).max()
	print(int(cost))

	return


def main():
	N, M, T = map(int, input().split())
	A = np.array(input().split(), np.int)
	abc = np.array([input().split() for _ in range(M)], np.int)
	# print(abc)
	solve(N, M, T, A, abc)


if __name__ == '__main__':
    main()
