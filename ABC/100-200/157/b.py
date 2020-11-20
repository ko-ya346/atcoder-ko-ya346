import itertools
A = list(itertools.chain.from_iterable([list(map(int, input().split())) for _ in range(3)]))

bingo = [0 for _ in range(9)]
N = int(input())

for i in range(N):
    b = int(input())
    for j in range(9):
        if b == A[j]:
            bingo[j] = 1

f = 0
for i in range(3):
    if sum(bingo[i:i+3]) == 3:
        f = 1
        break
    elif sum(bingo[i::3]) == 3:
        f = 1
        break

if sum(bingo[0::4]) == 3:
    f = 1
elif sum(bingo[2:7:2]) == 3:
    f = 1

if f:
    print("Yes")
else:
    print("No")

'''
1 2 3
4 5 6 
7 8 9
3
1
4
7
'''