N = int(input())
AB = []
B = 0
for _ in range(N):
    a, b = map(int, input().split())
    AB.append(a+b)
    B += b
AB.sort(reverse=True)
print(sum(AB[::2])-B)