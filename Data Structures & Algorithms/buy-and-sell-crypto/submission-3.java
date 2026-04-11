class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0]; // Initialize minPrice to the value of day 0
        int maxProfit = 0; // Initialize maxProfit to 0;

        for(int i = 0; i < prices.length; i++) { // Loop through prices array
            maxProfit = Math.max(maxProfit, prices[i] - minPrice); // Check for maximum profit each day
            
            if(minPrice > prices[i]) { // If the current min price is greater than the value at the current index
                minPrice = prices[i]; // Make the value at the current index the new min price
            }
        }
        return maxProfit; // return the maximum profit attainable from the prices array 
    }
}
