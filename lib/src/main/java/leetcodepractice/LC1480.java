package leetcodepractice;

/**
 * <a href="https://leetcode.com/problems/running-sum-of-1d-array/">LeetCode No.1480</a>
 */
public class LC1480 {
    public int[] runningSum(int[] nums) {
        var result = new int[nums.length];
        result[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            result[i] = result[i - 1] + nums[i];
        }
        return result;
    }

}
