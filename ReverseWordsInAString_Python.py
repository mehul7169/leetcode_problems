class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split(" ")
        strList.reverse()
        result = ' '.join(str(x) for x in strList if x is not '')
        return result