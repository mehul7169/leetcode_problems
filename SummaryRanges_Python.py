class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def getString(self, l, r):
            if l == r:
                return str(l)
            return (str(l) + "->" + str(r))
        
        if not nums:
            return []
        l = r = nums[0] 
        res = []

        for num in nums[1:]:
            if num == r + 1:
                r = num
            else:
                res.append(getString(self, l,r))
                l = r = num
        res.append(getString(self, l, r))                
        return res