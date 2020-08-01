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

seg = segment_tree(10**5, min, 10**9)
arr = [i for i in range(10**5)]

for i,a in enumerate(arr):
    seg.update(i, a)
print(seg.query(333, 10**4))