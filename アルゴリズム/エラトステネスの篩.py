import math

#範囲内の素数を全列挙
def eratosthenes(limit):
    #範囲内の数字全て
    A = [i for i in range(2, limit+1)]
    P = []
    time = 0

    while True:
        prime = min(A)

        #最大値のルートが最小値になったら終わり
        if prime > math.sqrt(limit):
            break
        
        #素数を配列Pに入れる
        P.append(prime)
        
        #A内にprimeで割り切れる数があれば取り除く
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
    
    return set(P+A)
