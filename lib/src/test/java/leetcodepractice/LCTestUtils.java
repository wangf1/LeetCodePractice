package leetcodepractice;

import org.junit.jupiter.api.Assertions;

import java.util.ArrayList;
import java.util.List;

class LCTestUtils {


    static ListNode buildNodeList(int[] values) {
        ListNode head = null;
        for (int i = values.length - 1; i >= 0; i--) {
            head = new ListNode(values[i], head);
        }
        return head;
    }

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
