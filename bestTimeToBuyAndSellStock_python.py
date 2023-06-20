class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        min = max = buy = sell = 0
        profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[min]:
                min = i
                max = i
            elif prices[i] > prices[max]:
                if prices[i] - prices[min] > profit:
                    sell = max = i
                    buy = min
                    profit = prices[sell] - prices[min]
                else:
                    max = i
        
        return profit