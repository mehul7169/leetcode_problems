class Solution:
    def getSum(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            n = self.getSum(n)
        return True