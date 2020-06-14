s = input()
t = input()

if s==t:
    print("same")
elif str.upper(s)==str.upper(t):
    print("case-insensitive")
else:
    print("different")