A, B, X = map(int, input().split())
#二部探索で購入できる最大のNを求める
#1回の計算で半分に絞れるので30回くらいの計算量で解ける

l, r = 0, 10**9+1
while r-l > 1:
    m = (l+r)//2
    t = A*m+B*len(str(m)) #狙いの価格
    if t <= x:
        l = m
    else:
        r = m
print(l)