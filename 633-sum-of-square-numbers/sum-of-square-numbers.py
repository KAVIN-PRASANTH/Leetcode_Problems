class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0,(c//2)+2):
            cal=c-(i*i)
            if cal<0:
                return False
            cal=math.sqrt(cal)
            cal=str(cal).split(".")
            cal=int(cal[1])
            if cal==0:
                return True
        return False
    
        
       
        