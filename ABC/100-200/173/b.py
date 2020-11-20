from collections import Counter

N = int(input())
S = Counter([input() for _ in range(N)])

print("AC x",S["AC"])
print("WA x", S["WA"])
print("TLE x", S["TLE"])
print("RE x", S["RE"])