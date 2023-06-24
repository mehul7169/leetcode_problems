class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif num == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif num == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            elif num == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            else:
                stack.append(int(num))
        return stack[0]