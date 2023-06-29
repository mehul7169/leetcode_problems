class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digit = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']
        }

        output = []

        def backtracking(cur, nums):
            nonlocal output
            if not nums:
                output.append(cur)
                return
            num = int(nums[0])
            for i in digit[num]:
                next = cur + i
                backtracking(next, nums[1:])

        backtracking('', digits)
        return output


