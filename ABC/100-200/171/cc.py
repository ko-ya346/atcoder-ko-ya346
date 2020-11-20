from string import ascii_lowercase

N = int(input())
l = []

while N != 0:
    N -= 1
    l.append(N%26)
    N //= 26
print("".join(ascii_lowercase[x] for x in l[::-1]))