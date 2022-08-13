package leetcodepractice;

// https://leetcode.com/problems/is-subsequence/
public class LC392 {
    public boolean isSubsequence(String s, String t) {
        int sPointer = 0, tPointer = 0;
        for (; sPointer < s.length(); sPointer++) {
            boolean matched = false;
            char cS = s.charAt(sPointer);
            while (tPointer < t.length()) {
                char cT = t.charAt(tPointer);
                tPointer++;
                if (cS == cT) {
                    matched = true;
                    break;
                }
            }
            if (!matched) {
                return false;
            }
        }
        return true;
    }
}
