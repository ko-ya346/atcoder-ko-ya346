N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

card = []
for _ in range(M):
    b, c = map(int, input().split())
    card.append((b, c))

N, M = map(int, input().split())

sorted(dictionary, key=lambda x: x[1])