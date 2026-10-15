class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int max_profit = 0;

        for(int right = 0; right < prices.length; right++) {
            if(prices[right] < prices[left]) {
                left = right;
            }
                max_profit = Math.max(max_profit, prices[right] - prices[left]);
        }
        return max_profit;
    }
}
