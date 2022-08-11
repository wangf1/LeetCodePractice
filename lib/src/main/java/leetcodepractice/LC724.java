package leetcodepractice;

import java.util.stream.IntStream;

/**
 * <a href="https://leetcode.com/problems/find-pivot-index/">LC 724</a>
 */
public class LC724 {
    public int pivotIndex(int[] nums) {
        int sumLeft = 0;
        int sumRight = IntStream.range(1, nums.length).reduce(0, (subtotal, element) -> subtotal + nums[element]);
        if (sumLeft == sumRight) {
            return 0;
        }
        for (int pivot = 1; pivot < nums.length; pivot++) {
            sumLeft += nums[pivot - 1];
            sumRight -= nums[pivot];
            if (sumLeft == sumRight) {
                return pivot;
            }
        }
        return -1;
    }
}
