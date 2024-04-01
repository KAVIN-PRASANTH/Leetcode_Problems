class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        s=list(filter(lambda x:x!=" ",list(s.split(' '))))
        return len(s[len(s)-1])
        