package leetcodepractice;

//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
public class LC121 {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int min = prices[0];

        for (int current : prices) {
            min = Math.min(min, current);
            profit = Math.max(current - min, profit);
        }

        return profit;
    }
}
