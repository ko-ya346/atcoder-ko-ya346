n = int(input())
a = list(map(int, input().split()))

P = [x for x in a if x>=0]
M = [x for x in a if x<0]

pare = []

ans = 0

if len(P)==0:
    while len(M)>1:
        M.sort(reverse=True)

        m1, m2 = M.pop(0), M.pop(-1)
        pare.append((m1, m2))
        M.append(m1-m2)
    ans = M[0]
elif len(M)==0:
    while len(P)>1:
        P.sort()
        p1 = P.pop(0)
        p2 = P.pop(0)
        pare.append((p2, p1))
        P.append(p2-p1)
    ans = P[0]
else:
    while len(P)>1:
        P.sort()
        M.sort(reverse=True)
        p = P.pop(0)
        m = M.pop(0)
        pare.append((m, p))
        M.append(m-p)
# print(M)
# print(P)
print(pare)
print(ans)    

# -1 -2 -4