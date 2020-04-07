N = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(N)]#玉を収納していくリスト

def check(i):
#Nには箱の番号（aのindex+1)を大きい順に入れる
    n = i
    cnt = 0
    #aaの倍数の箱に入っている玉の数をカウント
    while n <= N:
        cnt += b[n-1]
        n += i
        #aaを2倍、3倍、、、としていく
    return cnt

for i in range(N-1, -1, -1):
    if (a[i]+check(i+1))%2 == 1:
        b[i] = 1
    
ans = sum(b)
ll = []
for i in range(N):
    if b[i] == 1:
        ll.append(i+1)

lll = [str(i) for i in ll]
if ans == 0:
    print(ans)
else:
    print(ans)
    print(" ".join(lll))