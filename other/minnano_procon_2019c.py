K, A, B = map(int, input().split())

if A+2>=B:
    ans = 1+K
else:
    k = K-A+1 #初回にA枚まで増やした後の回数
    ans = A + k//2 * (B-A)
    if k%2:
        ans += 1
print(ans)