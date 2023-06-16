class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(currentState) - 1):
            if currentState[i:i+2] == '++':
                new = currentState[:i] + '--' + currentState[i+2:]
                result.append(new)

        return result