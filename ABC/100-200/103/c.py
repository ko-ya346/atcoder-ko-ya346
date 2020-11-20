Q, H, S, D = map(int, input().split())
N = int(input())

cost = [Q, min(Q*2, H), min(Q*4, H*2, S), min(Q*8, H*4, S*2, D)]

print(N//2*cost[3] + N%2*cost[2])