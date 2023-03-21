class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translateDict = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }
        result = 0
        while len(s) != 0:
            print(s)
            subString = ""
            if len(s) != 1:
                subString = s[0:2]
            if subString in translateDict:
                result += translateDict[subString]
                s = s[2:]
            else:
                result += translateDict[s[0]]
                s = s[1:]
        return result