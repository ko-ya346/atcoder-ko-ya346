n = int(input())
a = [0] + list(map(int,input().split()))

#A1 ... AnのBIT(1-indexed)
BIT = [0]*(n+1)

#A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        print(idx)
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum

#Ai += x O(logN)
def BIT_update(idx,x):
    while idx <= n:
        BIT[idx] += x
        idx += (idx&(-idx))
    return

ans = 0
for j in range(1, n+1):
    print(BIT)
    ans += j - 1 - BIT_query(a[j])
    BIT_update(a[j], 1)

print(ans)
