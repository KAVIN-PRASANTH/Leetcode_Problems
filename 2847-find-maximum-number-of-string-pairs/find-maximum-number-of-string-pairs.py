from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        m=list(map(lambda e:"".join(sorted(list(e))),words))
        m.sort()
        map1=Counter(m)
       
        p=0
        for key,val in map1.items():
            p+=val//2

        return p
        