class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] # Set the min price to first day
        best_profit = 0 # Initialize the best profit to 0

        for i in range(len(prices)): # Loop through prices list
            if min_price > prices[i]: # If the min price is > current price, set the new min price as current price
                min_price = prices[i]
            else: # Else, find the best max profit between current best_profit and that new day's profit
                best_profit = max(best_profit, prices[i] - min_price)
        return best_profit