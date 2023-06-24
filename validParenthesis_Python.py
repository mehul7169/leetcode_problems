class Solution:
    def isValid(self, s: str) -> bool:
        first = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for i in s:
            if i in first.values():
                stack.append(i)
            else:
                try:
                    curr = stack.pop()
                except:
                    return False
                if first[i] != curr:
                    return False
        if len(stack) == 0:
            return True
        return False