class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l, r = 0, len(height) - 1

        while l < r:
            small = min(height[r], height[l])
            area = ((r-l) *small)
            if area > max: max = area

            if height[r] < height[l]: r -= 1
            else: l+=1

        return max