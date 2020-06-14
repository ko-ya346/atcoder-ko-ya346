# G - 組分け

import itertools
import sys
readline = sys.stdin.readline

N = int(input())

#引数1の数字をN個並べたデカルト積を返す
for i in itertools.product([0, 1, 2], repeat=N):
    for j, k in itertools.combinations(range(N), 2):
        print("i", i)
        print("j", j, "k", k)