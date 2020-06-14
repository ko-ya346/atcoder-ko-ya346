import numpy as np

N, M, X = map(int, input().split())

C = [list(map(int, input().split())) for _ in range(N)]
# print(C)
sum_C = np.sum(C,axis=0)
# print(sum_C)

if np.any(sum_Ccopy[1:] < X):
    print(-1)
    exit()

cost = float("inf")
for ij in [0, 1]:
    for ii in [0, 1]:
        for i in range(M+1):
            cc = sorted(C, key=lambda x:x[0], reverse=ij)
            ccc = np.array(sorted(cc, key=lambda x:x[i], reverse=ii))
            # print("ccc", ccc)
            sum_Ccopy = np.zeros(M+1)
            for j in range(N):
                sum_Ccopy += ccc[j]
                # print(np.all(sum_Ccopy[1:] >= X))
                # print(sum_Ccopy[0])
                if np.all(sum_Ccopy[1:] >= X):
                    cost = min(cost, sum_Ccopy[0])
                    # print(sum_Ccopy[0])
                    # print("sum_Ccopy", sum_Ccopy)
                # print(cost)
    
print(int(cost))
 

