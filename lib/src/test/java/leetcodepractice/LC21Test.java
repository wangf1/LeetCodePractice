package leetcodepractice;

import leetcodepractice.LC21.ListNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class LC21Test {

    private LC21 testee;

    private static void verifyMergedList(List<Integer> expectedValues, ListNode merged) {
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

    @BeforeEach
    void setUp() {
        testee = new LC21();
    }

    @Test
    void mergeTwoLists() {
        // Input: list1 = [1,2,4], list2 = [1,3,4]
        // Output: [1,1,2,3,4,4]
        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4, null)));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4, null)));
        ListNode merged
                = testee.mergeTwoLists(list1, list2);
        verifyMergedList(Arrays.asList(1, 1, 2, 3, 4, 4), merged);

        // Input: list1 = [], list2 = []
        //         Output: []
        merged = testee.mergeTwoLists(null, null);
        verifyMergedList(null, merged);

        // Input: list1 = [], list2 = [0]
        // Output: [0]
        merged = testee.mergeTwoLists(null, new ListNode(0, null));
        verifyMergedList(List.of(0), merged);
    }
}
