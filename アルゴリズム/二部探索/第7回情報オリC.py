import bisect

N,M=map(int, input().split())
point = sorted([int(input()) for _ in range(N)])

ans = []

for i in point:
    if i <= M:
        ans.append(i)
    else:
        break
    for j in point:
        if i+j <= M:
            ans.append(i+j)
        else:
            break
        for k in point:
            cnt = i+j+k
            if cnt <= M:
                ans.append(cnt)
                num = bisect.bisect_left(point, M-cnt)
                if num > 0:
                    cnt += point[num-1]
                    if cnt <= M:
                        ans.append(cnt)
            else:
                break
            

a = 0
for ii in ans:
    if ii<= M:
        a = max(a, ii)
print(a)