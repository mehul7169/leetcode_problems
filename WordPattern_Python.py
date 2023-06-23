class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        letter_mapping = {}
        
        for letter, word in zip(pattern, words):
            if letter not in letter_mapping and word not in letter_mapping.values():
                letter_mapping[letter] = word
            elif letter not in letter_mapping or letter_mapping[letter] != word:
                return False
        return True