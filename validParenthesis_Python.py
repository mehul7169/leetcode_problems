class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        for i in range (len(s) - 1):
            if s[i] == "[" and s[i+1] == "]":
                newString = s[0:i] + s[i+2:]
                return self.isValid(newString)
            elif s[i] == "(" and s[i+1] == ")":
                newString = s[0:i] + s[i+2:]
                return self.isValid(newString)
            elif s[i] == "{" and s[i+1] == "}":
                newString = s[0:i] + s[i+2:]
                return self.isValid(newString)
        return False