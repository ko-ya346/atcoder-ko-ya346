n = int(input())
flag = False
for i in range(n//4+1):
    for j in range(n//7+1):
        if 4*i+7*j == n:
            flag = True
            break
    else:
        continue
    break

if flag:
    print("Yes")
else:
    print("No")