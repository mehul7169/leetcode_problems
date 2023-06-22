class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = ""
        found = {}
        curr = ""
        for i in s:
            if i in found:
                if len(curr) >= len(long):
                    long = curr
                ind = curr.index(i)
                curr = curr[ind + 1:] + i
                print(curr)
                found = {i : 1 for i in curr}
            else:
                found[i] = 1
                curr += i
        
        if len(curr) >= len(long):
            return len(curr)
        return len(long)