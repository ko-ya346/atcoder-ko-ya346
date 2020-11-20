from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
a = list(map(int, input().split()))

a_cnt = Counter(a)

a_comb = {}
for key, val in a_cnt.items():
    if val >= 2:
        a_comb[key] = combinations_count(val, 2)
    else:
        a_comb[key] = 0

sum_v = sum(a_comb.values())

for num in a:
    print(sum_v-a_cnt[num]+1)