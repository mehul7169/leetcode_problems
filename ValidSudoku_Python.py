class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isElemValid(row, column, board):
            num = board[row][column]
            for i in range(9):
                if (num == board[row][i] and i != column) or (num == board[i][column] and i != row):

                    return False

            frow = row - (row % 3)
            fcol = column - (column % 3)
            
            for i in range(3):
                if (num == board[frow + i][fcol] and not (frow + i == row and fcol == column)) or (num == board[frow + i][fcol + i] and not (frow + i == row and fcol + i == column)) or (num == board[frow][fcol + i] and not (frow == row and fcol + i== column)):
                    return False
            
            if (num == board[frow + 2][fcol + 1] and not (frow + 2 == row and fcol + 1== column)) or (num == board[frow + 1][fcol + 2] and not (frow + 1 == row and fcol + 2 == column)): return False

            return True
        for i,row in enumerate(board):
            for j in range(len(row)):
                if board[i][j] == ".":
                    continue
                elif not isElemValid(i, j, board):
                    return False
        return True
                