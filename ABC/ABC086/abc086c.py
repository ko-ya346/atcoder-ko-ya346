n = int(input())
x = [input().split() for i in range(n)]

mm = 0
flag = 1

if int(x[0][0]) < int(x[0][1]) + int(x[0][2]):
    flag = 0
else:
    if int(x[0][0])%2 != (int(x[0][1]) + int(x[0][2]))%2:
        flag = 0
    else:
        for i in range(n-1):
            if int(x[i+1][0])-int(x[i][0]) < int(x[i+1][1]) +int(x[i+1][2])-int(x[i][1])-int(x[i][2]):
                flag = 0
                break
            else:
                if (int(x[i+1][0])-int(x[i][0]))%2 != (int(x[i+1][1]) +int(x[i+1][2])-int(x[i][1])-int(x[i][2]))%2:
                    flag = 0
                    break            

if flag == 1:
    print("Yes")
else:
    print("No")
    

