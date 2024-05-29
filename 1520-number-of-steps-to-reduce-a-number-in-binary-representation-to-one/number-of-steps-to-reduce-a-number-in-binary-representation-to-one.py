class Solution:
    def numSteps(self, s: str) -> int:
        step=0
        li=list(map(lambda x:int(x,2),list(s)))
        def addone():
            lim=len(li)-1
            while li[lim]==1 and lim>=0:
                li[lim]=0
                lim-=1
            if lim==-1:
                li.insert(0,1)
            else:
                li[lim]=1

        while len(li)!=1:
            l=len(li)-1
            if li[l]==1:
                addone()
            else:
                li.pop()
            step+=1
            print(li)

        return step
        

        
        
        