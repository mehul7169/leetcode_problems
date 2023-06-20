class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        i = 0
        while i <(len(haystack)-needleLen+1):
            shortString = haystack[i:i+needleLen]
            if(shortString == needle):
                return i
            i+=1
        return -1