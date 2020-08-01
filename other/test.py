import numpy as np
from numba import njit
 
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())), dtype=np.int64)
 
@njit
def imos(a):
  b = np.zeros(n+1, dtype=np.int64)
  for i in range(n):
    l = max(0, i-a[i])
    r = min(i+a[i]+1, n)
    b[l] += 1
    if r <= n-1: b[r] -= 1
  
  b = np.cumsum(b)[:-1]
  return b
 
for q in range(k):
  a = imos(a)
  if np.min(a)==n:
    break
    
print(*a)
