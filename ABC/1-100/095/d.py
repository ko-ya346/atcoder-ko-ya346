from itertools import accumulate

n, c = map(int, input().split())

xv = [list(map(int, input().split())) 
        for _ in range(n)]

cw_acc = [0] * (n+1)
ccw_acc = [0] * (n+1)
cw_prev = 0
ccw_prev = c

for i in range(n):
    k = n - i - 1
    cw_acc[i+1] = cw_acc[i] + xv[i][1] - (xv[i][0] - cw_prev)
    cw_prev = xv[i][0]
    ccw_acc[i+1] = ccw_acc[i] + xv[k][1] - (ccw_prev - xv[k][0])
    ccw_prev = xv[k][0]

cw_acc = list(accumulate(cw_acc, max))
ccw_acc = list(accumulate(ccw_acc, max))
ans = 0
# print(cw_acc)
# print(ccw_acc)
# print(xv)

for i in range(n):
    k = n-i-1
    ans = max(
        ans,
        cw_acc[i + 1],
        cw_acc[i + 1] - xv[i][0] + ccw_acc[k],
        ccw_acc[i + 1],
        ccw_acc[i + 1] - (c - xv[k][0]) + cw_acc[k],
    )
print(ans)