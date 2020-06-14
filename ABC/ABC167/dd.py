N, K = map(int, input().split())

A = list(map(int, input().split()))

ord = [-1 for _ in range(N+1)]
v = 1
root = []

while ord[v] == -1:
    #ordに何回目のワープかが記録される
    ord[v] = len(root)
    #ワープの軌跡を記録
    root.append(v)
    #次の地点にワープ
    v = A[v-1]

# print("len(root)", len(root))
# print("ord[v]", ord[v])
# print("ord", ord)
# print("root", root)

#ord[v]:最終地点（ループ起点 or ループ前の道のり）
l = ord[v]
#ループ距離
c = len(root) - l

if K < l:
    #ループ前にワープが終了した場合、最終地点を出力
    ans = root[K]
else:
    #ループする回数を計算
    K -= l
    K %= c
    res = root[l+K]
print(res)

