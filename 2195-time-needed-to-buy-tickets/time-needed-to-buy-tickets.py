class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        c=0
        p=0
        for i in tickets:
            p=p+1
            if i>=tickets[k] and p>k:
                print("one")
                c=c+tickets[k]-1
            elif i>tickets[k]:
                print("two")
                c=c+tickets[k]
            else:
                print("three")
                c=c+i
            print(c)
        return c+1