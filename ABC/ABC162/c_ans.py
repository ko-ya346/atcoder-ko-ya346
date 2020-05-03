import math
from functools import reduce
from itertools import combinations_with_replacement
 
K = int(input())
 
def GCD(x):
    #与えられたlist内全ての数字の最大公約数を求める
    return reduce(math.gcd, x)
 
s = 0

#K以下の数字を3つ並べたtapleを生成 
for x in combinations_with_replacement(range(1, K + 1), 3):
    print(x)
    if x[0] == x[1] == x[2]:
        s += GCD(x)
    elif x[0] == x[1] or x[1] == x[2] or x[0] == x[2]:
        s += GCD(x) * 3
    else:
        s += GCD(x) * 6
 
print(s)