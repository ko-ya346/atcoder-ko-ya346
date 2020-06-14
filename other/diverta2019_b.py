from time import time

def main():
    total_time1 = 0
    for _ in range(100000):
        start = time()
        R, G, B, N = 1, 2, 3, 4

        cnt = 0
        for r in range(N//R + 1):
            for b in range(N//B + 1):
                res = (N - r*R - b*B)
                if res >= 0 and res%G == 0:
                    cnt += 1
        # print(cnt)

        total_time1 += time()-start
    print("main() time", total_time1/30)
if __name__ == "__main__":
    main()

total_time2 = 0
for _ in range(100000):
    start = time()
    R, G, B, N = 1, 2, 3, 4

    cnt = 0
    for r in range(N//R + 1):
        for b in range(N//B + 1):
            res = (N - r*R - b*B)
            if res >= 0 and res%G == 0:
                cnt += 1
    # print(cnt)

    total_time2 += time()-start
print("time", total_time2/30)


'''
R, G, B, N = map(int, input().split())

cnt = 0
for r in range(N//R + 1):
    for b in range(N//B + 1):
        res = (N - r*R - b*B)
        if res >= 0 and res%G == 0:
            cnt += 1
print(cnt)
'''