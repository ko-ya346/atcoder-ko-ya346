n = int(input())
ng = [int(input()) for _ in range(3)]

f = 0
for _ in range(100):
    if n in ng:
        break
    if n == 0:
        f = 1
        break
    if n-3 not in ng and n-3 >= 0:
        n -= 3
    elif n-2 not in ng and n-2 >= 0:
        n -= 2
    elif n-1 not in ng and n-1 >= 0:
        n -= 1
    else:
        break
if n == 0:
    f = 1
print("YNEOS"[f^1::2])