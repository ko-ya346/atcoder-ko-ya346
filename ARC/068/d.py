from collections import Counter

N = int(input())
A = (list(map(int, input().split())))

dic = Counter(A)
unique = len(dic)

print(unique if unique%2 else unique-1)