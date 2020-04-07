s = input()

n = int(input())

a = list(map(int, input().split()))

a = [int(input()) for _ in range(n)]

a = [input().split() for _ in range(n)]

X = [list(map(int, input().split())) for _ in range(n)]

dic = {}
for i in range(n):
	if a[i] not in dic:
		dic[a[i]] = 1
	else:
		dic[a[i]] += 1