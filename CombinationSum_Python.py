class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        outputSorted = set()

        def backtracking(cur):
            nonlocal output, outputSorted
            if sum(cur) > target:
                return
            elif sum(cur) == target and cur not in output:
                output.append(cur)
                return

            for i in candidates:
                dummy = cur[:]
                dummy.append(i)
                dummy.sort()
                backtracking(dummy)

        backtracking([])
        return output
