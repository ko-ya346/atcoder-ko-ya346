def kaibun(s):
    flag = 1
    ss = list(s)
    sss = ss.copy()
    ss.reverse()
    if sss != ss:
        flag = 0
    return flag

S = input()
N = len(S)
s1 = S[:(N-1)//2]
s2 = S[(N+3)//2-1:]

if kaibun(S)+kaibun(s1)+kaibun(s2) == 3:
    print("Yes")
else:
    print("No")