# n = int(input())
# a = [0] + list(map(int,input().split()))
n = 6
a = [1,2,3,4,5,6]


#A1 ... AnのBIT(1-indexed)
BIT = [0]*(n+1)

#A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        # print(idx)
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum

#Ai += x O(logN)
def BIT_update(idx,x):
    while idx <= n:
        BIT[idx] += x
        idx += (idx&(-idx))
    return

for i,e in enumerate(a):
       BIT_update(i+1,e)

#A1~A3の和 : 6
print(BIT_query(3))

#A3~A6の和 : 18
print(BIT_query(6)-BIT_query(2))
