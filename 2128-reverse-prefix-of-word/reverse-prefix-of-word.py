class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=word.find(ch)
        if a==-1:
            return word
        return word[a::-1]+word[a+1:len(word)]

        