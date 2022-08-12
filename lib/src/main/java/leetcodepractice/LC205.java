package leetcodepractice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class LC205 {

    /**
     * Two dictionary approach: Verify two String can transform to each other.
     */
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> mapStoT = new HashMap<>();
        Map<Character, Character> mapTtoS = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char cS = s.charAt(i);
            char cT = t.charAt(i);
            mapStoT.putIfAbsent(cS, cT);
            mapTtoS.putIfAbsent(cT, cS);

            if (!(mapStoT.get(cS) == cT && mapTtoS.get(cT) == cS)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Transform approach: Transform two strings to same int array
     */
    public boolean isIsomorphic1(String s, String t) {
        int[] intsS = transformToFirstIndexIntArray(s);
        int[] intsT = transformToFirstIndexIntArray(t);
        return Arrays.equals(intsS, intsT);
    }

    private int[] transformToFirstIndexIntArray(String s) {
        int[] result = new int[s.length()];
        Map<Character, Integer> cToFirstIndexMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            cToFirstIndexMap.putIfAbsent(c, i);
            result[i] = cToFirstIndexMap.get(c);
        }
        return result;
    }
}
