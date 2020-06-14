N, L = map(int, input().split())
x = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N)