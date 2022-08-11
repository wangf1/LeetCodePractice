package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC724Test {

    private LC724 testee;

    @BeforeEach
    void setUp() {
        testee = new LC724();
    }

    @Test
    void pivotIndex() {
        Assertions.assertEquals(3, testee.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));
        Assertions.assertEquals(-1, testee.pivotIndex(new int[]{1, 2, 3}));
        Assertions.assertEquals(0, testee.pivotIndex(new int[]{2, 1, -1}));
        Assertions.assertEquals(5, testee.pivotIndex(new int[]{-1, -1, 0, 1, 1, 0}));
    }
}
