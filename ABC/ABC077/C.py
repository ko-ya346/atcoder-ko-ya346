from bisect import bisect, bisect_left
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for i in B:
    max_A = bisect(A, i-1)
    min_C = bisect_left(C, i+1)
    # print("m_A", max_A, "m_C", min_C)
    ans += (max_A)* (len(C) - min_C)
print(ans)