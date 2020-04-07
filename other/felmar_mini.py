import random

def felmar(n):
    num = random.randrange(1, n)
    print("num = {}".format(num))
    return num**(n-1)%n

print(felmar(int(input())))