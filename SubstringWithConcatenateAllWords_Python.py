from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def isPermutation(self, s, words):
            count = defaultdict(int)
            wordLength = len(words[0])
            for i in range(len(s) // wordLength):
                curr = s[i*wordLength:(i+1) * wordLength]
                if curr in words and count[curr] != words.count(curr):
                    count[curr] += 1
                else:
                    return False
            return True

        
        # if len(s) < len(words) * len(words[0]): return []
        substringLength = len(words) * len(words[0])
        result = []
        for i in range(len(s) - (substringLength) + 1):
            sub = s[i: i + substringLength]
            add = isPermutation(self, sub, words)
            if add:
                result.append(i)

        return result