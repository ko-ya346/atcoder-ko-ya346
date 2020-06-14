S = input()
abc = [chr(i) for i in range(ord("a"), ord("z")+1)]

if len(S) == 26:
    for i in range(24, -1, -1):
        #後ろから文字に注目
        cand = list(S[i+1:])
        # print(f"cand {cand}")
        cand.sort()
        for c in cand:
            #大きい文字があった場合、挿げ替える
            if ord(c) > ord(S[i]):
                print(S[:i]+c)
                exit()
    print(-1)
else:
    for l in abc:
        if l not in S:
            print(S+l)
            exit()