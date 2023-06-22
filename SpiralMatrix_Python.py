class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        result = []
        while len(matrix) != 0:
            if (count == 0):
                lst = matrix[0]
                [result.append(x) for x in lst]
                matrix.pop(0)
            elif (count == 1):
                i = 0
                while i < len(matrix):
                    if len(matrix) == 0:
                        break
                    result.append(matrix[i][-1])
                    del matrix[i][-1]
                    if len(matrix[i]) == 0:
                        del matrix[i]
                        i-=1
                    i += 1
            elif (count == 2):
                lst = matrix[-1]
                lst.reverse()
                [result.append(x) for x in lst]
                matrix.pop(-1)
            elif count == 3:
                i = -1
                while i*-1 < len(matrix):
                    result.append(matrix[i][0])
                    del matrix[i][0]
                    if len(matrix[i]) == 0:
                        del matrix[i]
                        if len(matrix) == 0:
                            break
                        i += 1
                    i -= 1
            count = (count + 1) % 4
        return result