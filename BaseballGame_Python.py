class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []
        for operation in operations:
            if operation == '+':
                scores.append(scores[-1] + scores[-2])
            elif operation == 'D':
                scores.append(scores[-1] * 2)
            elif operation == 'C':
                scores.pop() 
            else:
                scores.append(int(operation))

        return sum(scores)