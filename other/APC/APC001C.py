def val():
    s = input()
    if s == "Vacant":
        exit()
    return 1 if s == "Male" else 0

N = int(input())

print(0, flush=True)

ofs = val()
l = 0
r = N

while True:
    m = (l+r)//2
    print(m, flush=True)
    s = val()^m & 1

    if ofs == s:
        l = m
    else:
        r = m
    