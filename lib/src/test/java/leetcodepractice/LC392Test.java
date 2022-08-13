package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC392Test {

    private LC392 testee;

    @BeforeEach
    void setUp() {
        testee = new LC392();
    }

    @Test
    void isSubsequence() {
        Assertions.assertTrue(testee.isSubsequence("abc", "ahbgdc"));
        Assertions.assertFalse(testee.isSubsequence("axc", "ahbgdc"));
    }
}
