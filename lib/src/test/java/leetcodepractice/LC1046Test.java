package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class LC1046Test {

    @Test
    void lastStoneWeight() {
        int result = new LC1046().lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1});
        Assertions.assertEquals(1, result);
    }
}
