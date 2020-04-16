import heapq  # heapqライブラリのimoprt

a = [1, 6, 8, 0, -1]
heapq.heapify(a)  # リストを優先度付きキューへ
print(a)

print(heapq.heappop(a))  # 最小値の取り出し
print(a)

heapq.heappush(a, -2)  # 要素の挿入
print(a)