class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for k in words:
            i,j=0,len(k)-1
           
            while(i<=j):
                
                if k[i]==k[j]:
                    i+=1
                    j-=1
                else:
                    break
               
            if i>j:
                return k
        return ""


        