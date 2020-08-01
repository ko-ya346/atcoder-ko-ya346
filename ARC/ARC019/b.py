A = list(input())
n = len(A)

if n == 1:
    print(0)
else:
    diff = 0
    ans = 0
    for i in range(n//2):
        if A[i] != A[-i-1]:
            diff += 1
            ans += 48
        else:
            ans += 50
    #diffが2以上の時はどう頑張っても回文にならない
    if diff >= 2:
        print(n*25)
        exit()

    if n%2 and diff != 0:
        ans += 25

    print(ans)