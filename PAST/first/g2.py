# G - 組分け

import itertools
import sys
readline = sys.stdin.readline

N = int(input())
A = [[0] * N for _ in range(N)]
for i in range(N-1):
    a = list(int(x) for x in input().split())
    A[i][i+1:] = a

print(A)

ans = 10**18 * -1

#全ての人が所属するグループのパターン全てを生成する
for i in itertools.product([0, 1, 2], repeat=N):
    tmp = 0
    print("i", i)

    #メンバーを2人ずつ比較して、同じグループに所属していた場合にスコアを足す
    for j, k in itertools.combinations(range(N), 2):
        print("j", j, "k", k)
        if i[j] == i[k]:
            tmp += A[j][k]
    ans = max(ans, tmp)

print(ans)
