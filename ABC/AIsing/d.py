#2回目以降のあまりを計算
def f(j):
    cnt = 0
    while j:
        j %= bin(j).count("1")
        cnt += 1
    return cnt

N = int(input())
S = input()

#入力を数値に変換
X = int(S, 2)

#元のbit数をカウント
pcx = S.count("1")
#bit数は-1, +1のみなので予め計算しておく
#カウントが0ならば0にしておく
pc1 = X % (pcx - 1) if pcx > 1 else 0
pc2 = X % (pcx + 1)

for i, y in enumerate(S):
    k = N - 1 - i
    if y == "0":
        print(f((pc2 + pow(2, k, pcx + 1)) % (pcx + 1)) + 1)
    elif pcx > 1:
        print(f((pc1 - pow(2, k, pcx - 1)) % (pcx - 1)) + 1)
    else:
        print(0)

