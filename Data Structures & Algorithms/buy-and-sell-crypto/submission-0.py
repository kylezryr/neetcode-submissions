class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        highest = 0

        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
                continue
            sellProfit = prices[i] - prices[left]
            if sellProfit > highest:
                highest = sellProfit

        return highest