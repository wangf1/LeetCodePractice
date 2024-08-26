package leetcodepractice;

public class LC63 {

    class Solution {

        public int uniquePathsWithObstacles(int[][] obstacleGrid) {

            int m = obstacleGrid.length;
            int n = obstacleGrid[0].length;

            if (obstacleGrid[m - 1][n - 1] == 1) {
                return 0;
            }

            int[][] dp = new int[m][n];
            dp[m - 1][n - 1] = 1;
            for (int c = n - 2; c >= 0; c--) {
                if (obstacleGrid[m - 1][c] == 0) {
                    dp[m - 1][c] = dp[m - 1][c + 1];
                }
            }
            for (int r = m - 2; r >= 0; r--) {
                if (obstacleGrid[r][n - 1] == 0) {
                    dp[r][n - 1] = dp[r + 1][n - 1];
                }
            }

            for (int r = m - 2; r >= 0; r--) {
                for (int c = n - 2; c >= 0; c--) {
                    if (obstacleGrid[r][c] == 0) {
                        dp[r][c] = dp[r + 1][c] + dp[r][c + 1];
                    }
                }
            }
            return dp[0][0];
        }
    }

}
