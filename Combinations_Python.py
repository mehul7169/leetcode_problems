class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtracking(cur, n, level, k):
            nonlocal output
            if level >= k:
                output.append(cur)
                return
            
            while(n):
                next = cur[:]
                next.append(n[0])
                backtracking(next, n[1:], level + 1, k)
                if len(n) > 0: n = n[1:]
        
        backtracking([], [i for i in range(1, n+1)], 0, k)

        return output