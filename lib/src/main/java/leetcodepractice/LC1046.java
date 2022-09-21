//https://leetcode.com/problems/last-stone-weight/

package leetcodepractice;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class LC1046 {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        heap.addAll(Arrays.stream(stones).boxed().collect(Collectors.toList()));
        while (heap.size() >= 2) {
            Integer heaviest = heap.poll();
            Integer secondHeaviest = heap.poll();
            assert secondHeaviest != null;
            int reminder = heaviest - secondHeaviest;
            if (reminder > 0) {
                heap.add(reminder);
            }
        }
        return heap.size() == 1 ? heap.poll() : 0;
    }
}
