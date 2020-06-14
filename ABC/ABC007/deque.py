from collections import deque

#dequeオブジェクト
d = deque()
print(d)

#右側に追加
d.append(1)
#左側に追加
d.appendleft(1)

#リストなどイテラブルオブジェクトの要素をすべて追加する
d.extend([2,3])
#extendleftは中身が逆転して左側に追加される
d.extendleft([4,5])

#要素を右側から取り出し
d.pop()
#左側から
d.popleft()