S = input()
abc = [chr(i) for i in range(ord("a"), ord("z")+1)]

if len(S) == 26:
    for i in range(24, -1, -1):
        cand = list(S[i+1:])
        print(f"cand {cand}")
        cand.sort()
        for c in cand:
            if ord(c) > ord(S[i]):
                print(S[:i]+c)
                exit()
    print(-1)
else:
    for l in abc:
        if l not in S:
            print(S+l)
            exit()