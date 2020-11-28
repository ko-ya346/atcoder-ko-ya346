from itertools import product

n, k = map(int, input().split())
xor = []
for i in range(n):
    T = list(map(int, input().split()))
    if i==0:
        xor.append(T)
    else:
        tmp = []
        for t in T:
            for x in xor[i-1]:
                tmp.append(t^x)
        xor.append(tmp)
if 0 in xor[-1]:
    print("Found")
else:
    print("Nothing")