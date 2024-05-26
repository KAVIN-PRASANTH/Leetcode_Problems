class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f="qwertyuiop"
        s="asdfghjkl"
        t="zxcvbnm"
        l=[]
        res=[f,s,t]
        b=-1
        for i in words:
            check=str(i[0]).lower()
            if check in f:
                b=0
            elif check in s:
                b=1
            else:
                b=2
            if b==-1:
                continue
            flag=-1
            print(f'b {b}')

            for j in range(1,len(i)):
                print(str(i[j]).lower() not in res[b])
                if str(i[j]).lower() not in res[b]:
                    flag=1
                    break
            print(f'flag : {flag}')
            if flag==-1:
                l.append(i)
        return l





        