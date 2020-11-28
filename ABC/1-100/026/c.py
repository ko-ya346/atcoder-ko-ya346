n = int(input())
G = [[] for _ in range(n)]
S = n*[1]
for i in range(1, n):
    b = int(input())-1
    # 部下の情報
    G[b].append(i)
for i in range(n-1, -1, -1):
    if G[i]:
        # 部下の給料リスト
        s = [S[g] for g in G[i]]
        S[i] = 1+min(s)+max(s)
print(S[0])