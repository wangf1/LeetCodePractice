package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class LC692Test {

    @Test
    void topKFrequent() {
        LC692 testee = new LC692();
        List<String> result;
        result = testee.topKFrequent(new String[]{"i", "love", "leetcode", "i", "love", "coding"}, 2);
        Assertions.assertEquals(Arrays.asList("i", "love"), result);

        result = testee.topKFrequent(new String[]{"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"}, 4);
        Assertions.assertEquals(Arrays.asList("the", "is", "sunny", "day"), result);
    }
}
