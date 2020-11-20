S = input()
N = len(S)

num = [0] * 2019
num[0] = 1
now, ans = 0, 0
_10 = 1


for i in range(N-1, -1, -1):
    now = (now + int(S[i]) * _10) % 2019
    print("now", now)
    _10 *= 10
    _10 %= 2019
    print("num[0]", num[0])
    ans += num[now]
    num[now] += 1
    
    print("ans",ans)
print(ans)