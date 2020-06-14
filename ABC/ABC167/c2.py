import numpy as np

N, M, X = map(int, input().split())

C = [list(map(int, input().split())) for _ in range(N)]
# print(C)
sum_C = np.sum(np.array(C),axis=0)
print(sum_C)

for num in sum_C:
    if num < X:
        print(-1)
        exit()

cost = float("inf")

for i in range(1, M+1):
    cc = sorted(C, key=lambda x:x[0], reverse=True)
    ccc = np.array(sorted(cc, key=lambda x:x[i]))
    print("ccc", ccc)
    sum_Ccopy = sum_C.copy()
    for j in range(N):
        sum_Ccopy -= ccc[j]
        print("sum_Ccopy", sum_Ccopy)
        # print(np.all(sum_Ccopy[1:] >= X))
        # print(sum_Ccopy[0])
        if np.any(sum_Ccopy[1:] < X):
            break
            # print(sum_Ccopy[0])
        cost = min(cost, sum_Ccopy[0])
        print(cost)
    
print(cost)


