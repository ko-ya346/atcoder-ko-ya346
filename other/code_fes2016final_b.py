N = int(input())

if N == 1:
    print(1)
else:
    s = 0
    l = []
    for i in range(1, N):
        s += i
        l.append(i)
        if s > N:
            break
    # print(l)

    for i in range(len(l)):
        if s-l[i] == N:
            l.pop(i)
            break

    for i in l:
        print(i)
