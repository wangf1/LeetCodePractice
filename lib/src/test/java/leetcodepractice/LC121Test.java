package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC121Test {

    private LC121 testee;

    @BeforeEach
    void setUp() {
        testee = new LC121();
    }

    @Test
    void maxProfit() {
        Assertions.assertEquals(5, testee.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
        Assertions.assertEquals(0, testee.maxProfit(new int[]{7, 6, 4, 3, 1}));
    }
}
