C = [3, 2, 1, 3, 0, 2]
CC = [1, 5, 10, 50, 100, 500]

A = 620
coin = 500
ans = 0

for i in range(6):
    print("maisuu", C[-i-1])
    print("coin", CC[-i-1])
    print("A", A)
    print("-----------")
    while C[-i-1] > 0 and A-CC[-i-1]>=0:
        A -= CC[-i-1]
        C[-i-1] -= 1
        ans += 1
print(ans)

