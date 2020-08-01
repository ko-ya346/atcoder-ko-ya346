from bisect import bisect

def bis(lis, n):
    l = 0
    r = len(lis)-1
    while r-l >= 1:
        mid = (l+r)//2
        if lis[mid] == n:
            return 1
        elif lis[mid] < n:
            l = mid+1
        else:
            r = mid

N = 3
M = 10
K = [1, 2]

k = []
for i in K:
    for j in K:
        k.append(i+j)
k.sort()
# l = 0
# r = N-1
print(k)

f = 0
for i in K:
    for j in K:
        aa = M-i+j
        # print("aa", aa)
        # print(bisect(k, aa))
        # if N-1 > bisect(k, aa)>0:
        if bis(k, M):
            f = 1
if f:
    print("Yes")
else:
    print("No")


