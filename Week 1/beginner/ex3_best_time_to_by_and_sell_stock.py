class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price, max_diff = prices[0], 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            max_diff = max(max_diff, price - lowest_price)

        return max_diff