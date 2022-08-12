package leetcodepractice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC205Test {

    private LC205 testee;

    @BeforeEach
    void setUp() {
        testee = new LC205();
    }

    @Test
    void isIsomorphic() {
        isIsomorphicTwoApproach("egg", "add", true);
        isIsomorphicTwoApproach("foo", "bar", false);
        isIsomorphicTwoApproach("paper", "title", true);
        isIsomorphicTwoApproach("badc", "baba", false);
    }

    private void isIsomorphicTwoApproach(String s, String t, boolean result) {
        Assertions.assertEquals(result, testee.isIsomorphic(s, t));
        Assertions.assertEquals(result, testee.isIsomorphic1(s, t));
    }
}
