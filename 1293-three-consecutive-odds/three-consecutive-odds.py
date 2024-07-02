class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res=0
        for i in arr:
            if i%2!=0:
                res+=1
            else:
                res=0
            if res==3:
                return True
        return False
        