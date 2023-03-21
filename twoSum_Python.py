class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checkList = {}
        for i in range(len(nums)):
            if (target - nums[i]) in checkList:
                return [checkList[target-nums[i]], i] 
            checkList[nums[i]] = i
        return []