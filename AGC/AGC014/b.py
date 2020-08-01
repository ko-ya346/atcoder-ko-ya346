from collections import Counter

N, M = map(int, input().split())
tree = []
for _ in range(M):
    a, b = map(int, input().split())
    tree.append(a)
    tree.append(b)

dic = Counter(tree)

f = 1
for v in dic.values():
    if v%2:
        f = 0
        break

if f:
    print("YES")
else:
    print("NO")
