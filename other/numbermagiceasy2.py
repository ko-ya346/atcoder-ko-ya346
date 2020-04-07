s = input()

def check(list, num):
    for i in range(8):
        if list[i] == num:
            return "Y"
    return "N"

A = [i for i in range(1,9)]
B = [1,2,3,4,9,10,11,12]
C = [1,2,5,6,9,10,13,14]
D = [i for i in range(16) if i%2 == 1]

for i in range(1, 17):
    if check(A, i) != s[0]:
        continue
    if check(B, i) != s[1]:
        continue
    if check(C, i) != s[2]:
        continue
    if check(D, i) != s[3]:
        continue
    print(i)
