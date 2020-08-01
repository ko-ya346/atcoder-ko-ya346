N = int(input())
if N <= 26:
    print(chr(ord("a") + N-(1)))

else:
    n = 1
    cnt = 0
    while n < N:
        cnt += 1
        n *= 26
    # print(cnt)
    ans = []
    while True:
        if cnt == 0:
            # print(N%26-1)
            if N%26:
                ans.append(chr(ord("a") + N%(26)-(1)))
                break
            else:
                # ans.append("z")
                break
        elif N == 0:
            ans.append("z")
        elif N//(26**cnt):
            if N%26**cnt:
            # print(N//(26**cnt)-1)
                ans.append(chr(ord("a") + N//(26**cnt)-1))
            else:
                ans.append("z")
            N %= 26**cnt
        cnt -= 1
        # print("N", N)

    print("".join(ans))



