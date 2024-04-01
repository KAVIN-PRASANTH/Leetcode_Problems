class Solution(object):
    def reverse(self, x):
        a=str(x)
        
        if a[0] == "-":
            if int(a[len(a)-1:0:-1])*-1<=-1*(2**31):
                return 0
            return int(a[len(a)-1:0:-1])*-1
        if int(a[len(a)-1::-1])>=(2**31)-1:
            return 0
        return int(a[len(a)-1::-1])
        