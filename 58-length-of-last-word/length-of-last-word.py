class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        s=list(filter(lambda x:x!=" ",list(s.split(' '))))
      #  print(s)
        print(s[len(s)-1])
        print(s[0])
        return len(s[len(s)-1])
        