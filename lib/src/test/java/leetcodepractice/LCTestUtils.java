package leetcodepractice;

import org.junit.jupiter.api.Assertions;

import java.util.ArrayList;
import java.util.List;

class LCTestUtils {
    static void verifyNodeList(List<Integer> expectedValues, ListNode merged) {
        if (merged == null) {
            Assertions.assertNull(expectedValues);
            return;
        }
        List<Integer> actualValues = new ArrayList<>();
        while (merged != null) {
            actualValues.add(merged.val);
            merged = merged.next;
        }
        Assertions.assertEquals(expectedValues, actualValues);
    }
}
