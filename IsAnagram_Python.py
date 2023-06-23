from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x,y = Counter(s), Counter(t)

        return x == y