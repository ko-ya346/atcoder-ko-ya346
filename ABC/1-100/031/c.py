N = int(input())
a = list(map(int, input().split()))

ans = -float("inf")

for i in range(N):
    aoki_max = -float("inf")
    aoki_max_ind = -1

    for j in range(N):
        if i==j:
            continue
        if i<j:
            l = a[i:j+1]
        else:
            l = a[j:i+1]
        if l:
            takahashi = sum(l[::2])
            aoki = sum(l[1::2])
            if aoki_max < aoki:
                aoki_max = aoki
                aoki_max_ind = j
    # print("i", i, "aoki_ind", aoki_max_ind)
    if aoki_max_ind != -1:
        if aoki_max_ind > i:
            n = i
            m = aoki_max_ind
        else:
            n = aoki_max_ind
            m = i
        # print(sum(a[n:m+1:2]))
        ans = max(ans, sum(a[n:m+1:2]))
    
print(ans)
    