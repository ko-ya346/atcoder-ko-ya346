A = list(input())

for i in range(2**3):
    num = int(A[0])
    ans = A[0]
    for j in range(3):
        if ((i >> j)&1):
           num += int(A[j+1])
           ans += "+"+A[j+1]
        else:
           num -= int(A[j+1])
           ans += "-"+A[j+1]
    if num == 7:
        print(ans+"=7")
        break