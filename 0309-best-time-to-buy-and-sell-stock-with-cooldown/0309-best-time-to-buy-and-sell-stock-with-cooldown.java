class Solution {
    public int maxProfit(int[] prices) {
        int hold = Integer.MIN_VALUE, sold = 0, rest = 0;
        for (int p : prices) {
            int h = Math.max(hold, rest - p);
            int s = hold + p;
            rest = Math.max(rest, sold);
            hold = h;
            sold = s;
        }
        return Math.max(sold, rest);
    }
}