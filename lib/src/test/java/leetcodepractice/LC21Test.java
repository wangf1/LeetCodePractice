package leetcodepractice;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static leetcodepractice.LCListTestUtils.buildNodeList;
import static leetcodepractice.LCListTestUtils.verifyNodeList;

class LC21Test {

    private LC21 testee;


    @BeforeEach
    void setUp() {
        testee = new LC21();
    }

    @Test
    void mergeTwoLists() {
        // Input: list1 = [1,2,4], list2 = [1,3,4]
        // Output: [1,1,2,3,4,4]
        ListNode list1 = buildNodeList(new int[]{1, 2, 4});
        ListNode list2 = buildNodeList(new int[]{1, 3, 4});
        ListNode merged
                = testee.mergeTwoLists(list1, list2);
        verifyNodeList(Arrays.asList(1, 1, 2, 3, 4, 4), merged);

        // Input: list1 = [], list2 = []
        //         Output: []
        merged = testee.mergeTwoLists(null, null);
        verifyNodeList(null, merged);

        // Input: list1 = [], list2 = [0]
        // Output: [0]
        merged = testee.mergeTwoLists(null, new ListNode(0, null));
        verifyNodeList(List.of(0), merged);
    }
}
