import sys
readline = sys.stdin.readline


N,K = map(int,readline().split())
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())), reverse=True)

ng = -1
#最大スコア
ok = F[0] * A[-1]

def isOk(x):
    print(x//F)
    # print(np.minimum(A, x // F))
    return A.sum() - np.minimum(A, x // F).sum() <= K
  
while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
    
print(ok)

