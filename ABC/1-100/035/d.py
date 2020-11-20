#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")
import heapq
from collections import defaultdict


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))


def shortestPath(g: Graph, s: int):
    dist = [INF]*g.N
    dist[s] = 0

    prev = [None]*g.N
    Q = []
    heapq.heappush(Q, (dist[s], s))

    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        for v, w in g.E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev


def solve(N: int, M: int, T: int,
          A: "List[int]",
          a: "List[int]", b: "List[int]", c: "List[int]"):

    g = Graph(N)
    g2 = Graph(N)
    for X, Y, Z in zip(a, b, c):
        g.add_edge(X-1, Y-1, Z)
        g2.add_edge(Y-1, X-1, Z)

    # N <= 10**5, M <= 10**5, T <= 10**9
    # 行きの道のり、帰りの道のりをダイクストラで求める O(NlogN)
    # 帰ってこられない節点を除く
    # コストを差し引いて最も稼げるところを求める O(N)
    forward_dist, forward_prev = shortestPath(g, 0)
    back_dist, back_prev = shortestPath(g2, 0)

    m = -INF
    for i in range(N):
        curr = 0
        cost = forward_dist[i] + back_dist[i]
        if T < cost:
            continue
        else:
            m = max(A[i]*(T-cost), m)
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, T, A, a, b, c)


if __name__ == '__main__':
    main()