class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        resmap={}
        final=[]
        for i in words[0]:
            if i in resmap:
                resmap[i]+=1
            else:
                resmap[i]=1
        words.pop(0)
        for i in words:
            check={}
            for j in i:
                if j in check:
                    check[j]+=1
                else:
                    check[j]=1
            for key,value in resmap.items():
                if key in check:
                    resmap[key]=min(check[key],value)
                else:
                    resmap[key]=0
        for key,value in resmap.items():
            for index in range(0,value):
                final.append(key)
        return final

                
            

        