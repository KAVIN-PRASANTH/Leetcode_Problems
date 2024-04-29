class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        res=str(bin(k)).replace('b','')
        a=list(map(lambda e:str(e).replace('b',''),list(map(bin,nums))))
        maxlen=max(list(map(lambda e:len(e),a)))
        if len(res)>maxlen:
            maxlen=len(res)
        print(maxlen)
        def eq(e):
            e=str(e)
            if len(e)!=maxlen:
                ex="0"*(maxlen-len(e))
                return ex+e
            return e
        a=list(map(eq,a))
        print(a)
        print(res)
        if len(res)!=maxlen:
            res=eq(res)
        for i in range(0,maxlen):
            count=0
            xor=0
            for k in a:
                xor^=int(k[i])
            if int(res[i])!=int(xor):
                c+=1
        
        return c

        