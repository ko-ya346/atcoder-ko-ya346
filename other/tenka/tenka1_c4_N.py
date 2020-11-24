N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        if (4*h*n-n*N-h*N) > 0:
            if n*h*N%(4*h*n-n*N-h*N) == 0:
                print(h, n, n*h*N//(4*h*n-n*N-h*N))
                exit()