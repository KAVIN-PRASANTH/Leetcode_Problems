class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        m=list(map(lambda e:"".join(sorted(list(e))),words))
        m.sort()
        map1={}
        for i in m:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        p=0
        for key,val in map1.items():
            p+=val//2
            
        print(map1)

        return p
        