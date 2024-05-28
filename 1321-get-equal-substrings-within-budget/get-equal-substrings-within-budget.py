class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i,j,length=0,0,len(s)
        maxvalue=0
        flag=0
        dum=maxCost
        while i<length and j<length:
            if i>j:
                j=i
            cost=abs(ord(s[j])-ord(t[j]))
            if cost==0:
                flag+=1
                j+=1
            elif maxCost-cost>=0:
                maxCost-=cost
                j+=1
                flag+=1
            else:
                if  maxCost+abs(ord(s[i])-ord(t[i]))<=dum:
                    maxCost+=abs(ord(s[i])-ord(t[i]))
                i+=1
                if flag>0:
                    flag-=1
            maxvalue=max(maxvalue,flag)
        return maxvalue





        