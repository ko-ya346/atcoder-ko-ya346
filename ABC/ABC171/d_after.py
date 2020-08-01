from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = [0 for _ in range(100005)]
for i in range(N):
    cnt[A[i]] += 1

sumA = sum(A)

# print(sumA)

Q = int(input())
for _ in range(Q):
    b, c = map(int, input().split())
    
    if cnt[b]:
        sumA += (c-b)*cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
    print(sumA)
