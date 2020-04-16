A, B, X = list(map(int, input().split()))

def bisect(cost):
    while True:
        if X-A*cost-B*len(str(cost)) >= 0:
            return min(cost, 1000000000)
        else:
            cost //= 2
print(bisect(X))