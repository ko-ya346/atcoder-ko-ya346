from collections import Counter

S = input()
if (("N" in S and "S" in S) or ("N" not in S and "S" not in S)) and (("E" in S and "W" in S) or ("E" not in S and "W" not in S)):
    print("Yes")
else:
    print("No")