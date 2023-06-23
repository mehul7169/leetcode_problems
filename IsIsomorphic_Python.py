class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashTable = {}

        for i in range(len(s)):
            hashVal = hashTable.get(s[i])
            if not hashVal and t[i] not in hashTable.values():
                hashTable[s[i]] = t[i]
            elif hashVal != t[i] or not hashVal:
                return False

            
        return True