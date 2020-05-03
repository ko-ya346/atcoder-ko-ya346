a = []
n = 0
while True:
    if n > 200000:
        break
    a.append(n)
    n += 2019
print(a)