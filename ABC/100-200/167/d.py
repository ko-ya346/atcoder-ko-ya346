N, K = map(int, input().split())

A = list(map(int, input().split()))

cnt = [-1 for _ in range(N)]
cnt[0] += 1

warp_rireki= [A[0]]

# c = 0
# print(cnt)
warp = A[0]-1
while cnt[warp-1] <= 1:
    # print(cnt[warp-1])
    cnt[warp] += 1
    warp = A[warp]-1

print("cnt", cnt)
# if K < len(warp_rireki):
#     print(warp_rireki[K])
# else:
#     print(roop[(K-one_root)%len(roop)-1])