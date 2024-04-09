class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        c=0
        p=0
        for i in tickets:
            p=p+1
            if i>=tickets[k] and p>k:
                c=c+tickets[k]-1
            elif i>tickets[k]:
                c=c+tickets[k]
            else:
                c=c+i
        return c+1