from math import ceil

N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0

for i in range(N-1):
    # print(ceil(i/2))
    ans += A[ceil(i/2)]


print(ans)

'''
8
1 2 3 4 5 6 7 8

7
1 2 3 4 5 6 7
'''