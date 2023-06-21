class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = [x for x in s if ('a' <= x <= 'z' or 'A' <= x <= 'Z' or '0' <= x <= '9')]
        if len(string) <= 1:
            return True
        for i in range(len(string) // 2 + 1):
            if len(string) <= 1:
                return True
            elif string[0] == string[-1]:
                string.pop(0)
                string.pop(-1)
            else:
                return False
