x, k, d = map(lambda x: abs(int(x)), input().split())

# 移動回数
move = min(x//d, k)
k -= move
x -= move * d

if k%2:
    print(d-x)    
else:
    print(x)
        