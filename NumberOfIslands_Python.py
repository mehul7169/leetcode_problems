class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, col):
            nr = len(grid)
            nc = len(grid[0])

            grid[row][col] = '0'

            if (row - 1 >= 0 and grid[row -1 ][col] == '1'): dfs(grid, row - 1, col)
            if (row + 1 < nr and grid[row + 1 ][col] == '1'): dfs(grid, row + 1, col)     
            if (col - 1 >= 0 and grid[row][col - 1] == '1'): dfs(grid, row, col - 1)
            if (col + 1 < nc and grid[row][col + 1] == '1'): dfs(grid, row, col + 1)

        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res+=1
                    dfs(grid, i, j)

        return res