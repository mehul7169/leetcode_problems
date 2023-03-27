class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new = 0
        pos = True
        if x < 0:
            pos = False
            x *= -1
        while (x != 0):
            new = (new * 10) + (x % 10)
            x = x // 10

        if not pos:
            new *= -1
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return new