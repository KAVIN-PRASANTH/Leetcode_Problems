class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a={}
        b={}
        res=[]
        for i in nums1:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in nums2:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        for x,y in a.items():
            if x in b:
                res.extend([x]*min(y,b[x]))
        return res
        
        