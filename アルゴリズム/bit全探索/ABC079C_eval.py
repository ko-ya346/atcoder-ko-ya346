A = input()
 
for i in range(2**3):
    ans = A[0]
    for j in range(3):
        if ((i >> j)&1):
           ans += "+"+A[j+1]
        else:
           ans += "-"+A[j+1]
    if eval(ans) == 7:
        print(ans+"=7")
        break