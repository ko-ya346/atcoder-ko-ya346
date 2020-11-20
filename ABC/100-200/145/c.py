from math import sqrt, factorial

N = int(input())
x = [list(map(int, input().split())) for _ in range(N)]

distance = 0
for i in range(N):
    for j in range(N):
        distance += sqrt((x[j][0]-x[i][0])**2 + (x[j][1]-x[i][1])**2)

print(distance/N)