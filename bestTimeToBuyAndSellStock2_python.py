class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = max = prices[0]

        for num in prices:
                
            if num > max:
                max = num
            elif num < max:
                profit += max - min
                min = max = num
        
        if min != max:
            profit += max- min
            
        return profit