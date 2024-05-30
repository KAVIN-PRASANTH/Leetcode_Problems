class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        c,n=0,len(arr)
        for i in range(0,n):
            xora=0
            for j in range(i+1,n):
                xora=xora^(arr[j-1])
                xorb=0
                for k in range(j,n):
                    xorb=xorb^(arr[k])
                    if xora==xorb:
                        c+=1
        return c
                    
        