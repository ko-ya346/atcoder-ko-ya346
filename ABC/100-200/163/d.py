N, K = map(int, input().split())

down = [0 for _ in range(N+2)]
for i in range(N+1):
    down[i+1] = down[i]+i

up = [0 for _ in range(N+2)]
for i in range(N, -1, -1):
    # print(i)
    up[-i-1] = up[-i-2]+i

print("down", down)
print("up", up)
print(up[K-2]-down[K])




