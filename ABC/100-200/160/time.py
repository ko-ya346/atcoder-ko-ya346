from time import time
start = time()
a = 0
for _ in range(1000000):
    a += 1
print(time()-start)

start = time()
a = ""
for _ in range(1000000):
    a += "a"
print(time()-start)

start = time()
a = []
for _ in range(1000000):
    a.append(1)
print(time()-start)