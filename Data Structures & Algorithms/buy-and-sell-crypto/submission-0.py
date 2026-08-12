class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mint = float('inf')
        maxProfit = 0
        for price in prices:
            profit = price - mint
            maxProfit = max(maxProfit, profit)
            mint = min(mint, price)
        return maxProfit