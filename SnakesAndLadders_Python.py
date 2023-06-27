class Solution:

    def returnNum(self, row, col, size):
        l = int(size ** 0.5)
        if row % 2 == l % 2:
            return size - (l * row) - col
        else: return size - (l * row) - (l - 1 - col)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = []
        queue = []
        size = len(board) * len(board[0])

        queue.append((1, 0))
        visited.append(1)

        ladder = {} 
        for i in range(len(board)): 
            for j in range(len(board)): 
                if board[i][j] != -1:
                    ladder[self.returnNum(i, j, size)] = board[i][j]

        print(ladder)

        while queue:
            print(queue)
            cur, step = queue.pop(0)
            if cur == size:
                return step
            for i in range(1, 7):
                new = cur + i
                
                if new in ladder:
                    new = ladder[new]
                if new not in visited: 
                    visited.append(new)
                    queue.append((new, step + 1))
                

        return -1