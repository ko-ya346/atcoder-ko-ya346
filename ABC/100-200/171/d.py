from collections import Counter

N = int(input())
A = list(map(int, input().split()))
sumA = sum(A)

dic = Counter(A)

Q = int(input())

for _ in range(Q):
    b, c = map(int, input().split())
    if b in dic.keys():
        sumA += ((c-b)*dic[b])

        #変更後の数字は既にいる？
        if c in dic.keys():
            #個数を保持
            #bの個数をcに追加し、bを削除
            dic[c] += dic[b]
            del dic[b]
        else:
            dic[c] = dic[b]
            del dic[b]
        # print("C", C)
        
        
        
        # print(dic)
    # else:
    #     ans = sumA
    print(sumA)