Na, Nb = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
# print(A|B)
print(len(A&B)/len(A|B))