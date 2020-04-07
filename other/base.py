base = int(input())
ans = []


for i in range(2, base):
    flag = 1
    for j in range(base):
        for k in range(base):
            for l in range(base):
                if (j*base*base+k*base+l)%i == 0 and (l+j+k)%i != 0:
                    flag = 0
    if flag == 1:
        ans.append(i)
print(ans)
