import numpy as np

h , w = map(int, input().split())
visited = np.zeros((h,w),dtype=int)

#白いマスは大きい数字入れておく
for y in range(h):
    _in = input()
    for x, value in enumerate(_in):
        if value == '.':
            visited[y][x] = 10**9
# print(visited)

for i in range(1,h):
    print("i", i)
    visited[i,:] = np.minimum(visited[i,:],visited[i-1,:]+1)
    print(visited[i,:])
print("step1", visited)

for i in reversed(range(h-1)):
    print("i", i)
    visited[i,:] = np.minimum(visited[i,:],visited[i+1,:]+1)
    print(visited[i,:])
print("step2", visited)

for j in range(1,w):
    visited[:,j] = np.minimum(visited[:,j],visited[:,j-1]+1)
    print(visited[:, j])
print("step3", visited)

for j in reversed(range(w-1)):
    visited[:,j] = np.minimum(visited[:,j],visited[:,j+1]+1)
    print(visited[:, j])
    
print("step4", visited)
print(np.max(visited))
