K, N = map(int, input().split())
a = list(map(int, input().split()))

distance = [a[0]+K-a[-1]]
for i in range(N-1):
    distance.append(a[i+1]-a[i])
print(K-max(distance))