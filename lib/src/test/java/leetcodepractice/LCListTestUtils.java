package leetcodepractice;

import com.google.common.primitives.Ints;
import org.junit.jupiter.api.Assertions;

import java.util.ArrayList;
import java.util.List;

class LCListTestUtils {


    static ListNode buildNodeList(int[] values) {
        ListNode head = null;
        for (int i = values.length - 1; i >= 0; i--) {
            head = new ListNode(values[i], head);
        }
        return head;
    }

    static ListNode buildNodeList(List<Integer> values) {
        int[] intArray = Ints.toArray(values);
        return buildNodeList(intArray);
    }

    static void verifyNodeList(List<Integer> expectedValues, ListNode head) {
        if (head == null) {
            Assertions.assertNull(expectedValues);
            return;
        }
        List<Integer> actualValues = new ArrayList<>();
        while (head != null) {
            actualValues.add(head.val);
            head = head.next;
        }
        Assertions.assertEquals(expectedValues, actualValues);
    }


}
