N = int(input())

a = [list(input()) for _ in range(N)]

# A = []

# for i in range(N):
#     s = []
#     for j in range(N):
#         s.append(a[j][i])
#     A.append(s)
# print(A)
ans = []

if N == 1:
    print(a[0][0])
else:
    for i in range(N//2):
        f = set(a[i]) & set(a[-i-1])
        # print(f)
        if not f:
            ans = 0
            break
        else:
            ans.append(list(f)[0])

    if ans:
        ans_r = ans.copy()
        ans_r.reverse()
        if N%2 == 0:
            print("".join(ans + ans_r))
        else:
            # print(ans)
            # print(ans_r)
            # print(list(a[N//2][0]))
            # print(ans)
            print("".join(ans[:N]) + a[N//2][0] + "".join(ans_r))
    else:
        print(-1)

