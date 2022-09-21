//https://leetcode.com/problems/top-k-frequent-words/

package leetcodepractice;

import java.util.*;

public class LC692 {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        Arrays.stream(words).forEach(w -> count.merge(w, 1, Integer::sum));
        List<Map.Entry<String, Integer>> sorted = new ArrayList<>(count.entrySet());
        sorted.sort((e1, e2) -> {
            int result = e1.getValue() - e2.getValue();
            if (result != 0) {
                return result;
            } else {
                return e2.getKey().compareTo(e1.getKey());
            }
        });
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= k; i++) {
            result.add(sorted.get(sorted.size() - i).getKey());
        }
        return result;
    }
}
