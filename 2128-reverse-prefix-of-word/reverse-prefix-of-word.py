class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j,i=0,0
        for i in range(0,len(word)):
            if word[i]==ch:
                break
        if i+1==len(word) and word[i]!=ch:
            return word
        return word[i::-1]+word[i+1:len(word)]

        