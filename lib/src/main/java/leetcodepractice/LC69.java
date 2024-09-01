package leetcodepractice;

public class LC69 {
    class Solution {
        public int mySqrt(int x) {

            int left = 0, right = x;
            while (left <= right) {
                int mid = (left + right) / 2;
                long square = (long) mid * mid;
                if (square == x) {
                    return mid;
                }
                if (square > x) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            long square = (long) left * left;
            if (square > x) {
                return left - 1;
            } else {
                return left;
            }
        }

    }
}

