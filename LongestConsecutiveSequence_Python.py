class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        uset = set(nums)
        maxi = 1
        for i in uset:
            if i-1 in uset:
                continue
            else:
                conseq = 1
                while i + conseq in uset:
                    conseq += 1
                maxi = max(maxi, conseq)
        return maxis