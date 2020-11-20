N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

if N == 2:
    ans = A[0]
elif N == 3:
    ans = sum(A[:2])
elif N == 4:
    ans = sum(A[:2])+A[1]
elif N == 5:
    ans = sum(A[:2])+A[1]+A[2]
elif N == 6:
    ans = sum(A[:2])+A[1]+A[2]*2
else:
    ans = sum(A[:2])+A[1]+A[2]*2
    print(ans)
    ind = N-6
    if ind%2 == 0:
        ans += sum(A[3:3+ind//2])*2
    else:
        ans += sum(A[3:3+ind//2])*2+A[3+ind//2]


print(ans)

'''
8
1 2 3 4 5 6 7 8

7
1 2 3 4 5 6 7
'''