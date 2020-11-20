s = input()
mod = 10**9+7

n = len(s)
#あまりの合計
res = [1] + [0]*12

for ss in s:
    dp = [0 for _ in range(13)]
    for i in range(13):
        #dp
        print(f"(10*i)%13 {(10*i)%13}, i {i}")
        dp[(10*i)%13] = res[i]
    #倍の長さにする
    dp += dp
    print("dp", dp)

    if ss == "?":
        for i in range(13):
            print(f"sum(dp[i+4:i+14]) {sum(dp[i+4:i+14])}")
            res[i] = sum(dp[i+4:i+14])
    else:
        for i in range(13):
            print(f"dp[i+13-int(ss)] {dp[i+13-int(ss)]}")
            res[i] = dp[i+13-int(ss)]
    print("res", res)

    #resのカウントをmodで割る
    res = [v%mod for v in res]
print(res[5])