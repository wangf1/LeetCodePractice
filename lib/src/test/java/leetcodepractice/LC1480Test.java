package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC1480Test {

    private LC1480 testee;


    @BeforeEach
    void setup() {
        testee = new LC1480();
    }

    @Test
    void runningSum() {
        int[] result1 = testee.runningSum(new int[]{1, 2, 3, 4});
        Assertions.assertArrayEquals(new int[]{1, 3, 6, 10}, result1);
    }

}
