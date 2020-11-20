N, M = map(int, input().split())

query = []
bridge = [1 for _ in range(N-1)]

for _ in range(M):
    a, b = map(int, input().split())
    query.append((a, b))

#街が左にある方を優先
query = sorted(query, key=lambda x: x[1])
#喧嘩する街が近い方を優先
# query = sorted(query, key=lambda x: x[2])

ans = 0
left = 0
for i, j in query:
    if left < i:
        left = j-1
        ans += 1

# print(bridge)
print(ans)