class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in dic:
                return [dic[num], i]
            else:
                dic[diff] = i
        return []