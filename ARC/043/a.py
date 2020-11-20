N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]

if max(S)-min(S) == 0:
    print(-1)
else:
    p = B/(max(S)-min(S))
    q = (N*A-sum(S)*p)/N
    print(p, q)