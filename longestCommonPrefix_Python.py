class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def findCommonPrefix(result, string):
            count = 0
            for i in range(min(len(result), len(string))):
                if result[i] == string[i]:
                    count += 1
                else:
                    break
                
            return result[0:count]

        result = strs[0]
        for string in strs[1:]:
            result = findCommonPrefix(result, string)
            if len(result) == 0:
                return ""

        return result
