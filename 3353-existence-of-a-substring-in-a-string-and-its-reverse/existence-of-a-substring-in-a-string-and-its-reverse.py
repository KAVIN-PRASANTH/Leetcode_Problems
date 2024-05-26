class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1,len(s)):
            string=s[i]+s[i-1]
            if string in s:
                return True
        return False
        