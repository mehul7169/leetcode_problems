class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True