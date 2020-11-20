class segment_tree:
    def __init__(self, N, operator_M, e_M):
        #演算子
        self.op_M = operator_M
        #単位元
        self.e_M = e_M
        
        self.N0 = 1<<(N-1).bit_length()
        self.dat = [self.e_M]*(2*self.N0)
    
    # 長さNの配列 initial で初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])

    # a_k の値を x に更新
    def update(self,k,x):
        k += self.N0
        self.dat[k] = x
        k //= 2
        while k:
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
            k //= 2

    # 区間[L,R]をopでまとめる
    def query(self,L,R):
        L += self.N0; R += self.N0 + 1 
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.dat[R],sr)
            if L & 1:
                sl = self.op_M(sl,self.dat[L])
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)

    def get(self, k): #k番目の値を取得。query[k,k]と同じ
        return self.dat[k+self.N0]


# coding: utf-8
# Your code here!

n,m = map(int, input().split())
pab = []
for _ in range(m):
    p,a,b = map(float, input().split())
    pab.append((int(p),float(a),float(b)))

sp = sorted({p for i,(p,a,b) in enumerate(pab)})
print(sp)
zaatu = {pi:i for i,pi in enumerate(sp)}
print(zaatu)
affine = lambda X,Y: (X[0]*Y[0],X[1]*Y[0]+Y[1])

seg = segment_tree(m, affine, (1,0))
print(seg.dat)

am = 1.0
aM = 1.0

for p,a,b in pab:
    seg.update(zaatu[p],(a,b))
    va,vb = seg.dat[1]
    am = min(am,va+vb)
    aM = max(aM,va+vb)

print(am)
print(aM)    
