def total(n):
    if n < 1:
        return 0

    return n + total(n-1)

print(total(int(input())))