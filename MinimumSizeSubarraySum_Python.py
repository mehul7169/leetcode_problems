class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = l = r = 0
        result = len(nums) + 1

        for num in nums:
            sum += num
            r += 1
            while sum >= target:
                result = min(result, r - l)
                sum -= nums[l]
                l += 1

        return result % (len(nums) + 1)