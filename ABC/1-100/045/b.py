a = list(input())
b = list(input())
c = list(input())

d = {"a": a,
     "b": b,
     "c": c}

key = "a"
while True:
    if len(d[key]):
        key = d[key].pop(0)
    else:
        break
print(key.upper())