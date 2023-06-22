class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rlen = len(matrix)
        clen = len(matrix[0])
        index = []
        for i, num in enumerate(matrix):
            for j, number in enumerate(num):
                if number == 0:
                    index.append([i,j])

        for ind in index:
            row = ind[0]
            col = ind[1]
            matrix[row][:] = [0] * clen
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        