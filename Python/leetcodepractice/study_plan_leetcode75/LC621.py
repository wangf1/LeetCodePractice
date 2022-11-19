# https://leetcode.com/problems/task-scheduler
import heapq
from collections import Counter


class Solution:
    # Use most often character (task) each time, by leveraging priority queue
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n <= 0:
            return len(tasks)

        c_count = Counter(tasks)
        count_c = [[-x[1], x[0]] for x in c_count.items()]

        heapq.heapify(count_c)

        schedule = []
        idle = 'idle'
        while count_c:
            tmp_count = []
            for _ in range(n + 1):
                if count_c:
                    curr_count = heapq.heappop(count_c)
                    schedule.append(curr_count[1])
                    curr_count[0] += 1
                    if curr_count[0] < 0:
                        tmp_count.append(curr_count)
                else:
                    schedule.append(idle)
            for c in tmp_count:
                heapq.heappush(count_c, c)

        while schedule[-1] == idle:
            schedule.pop()  # remove tailing 'idle'
        print(schedule)
        return len(schedule)

    # Simplified version, remove the task queue "schedule" since not really necessary.
    def leastInterval2(self, tasks: list[str], n: int) -> int:
        if n <= 0:
            return len(tasks)

        c_count = Counter(tasks)
        count_c = [-x for x in c_count.values()]
        heapq.heapify(count_c)

        time = 0
        while count_c:
            tmp_count = []
            for _ in range(n + 1):
                if count_c:
                    curr_count = heapq.heappop(count_c)
                    time += 1
                    curr_count += 1
                    if curr_count < 0:
                        tmp_count.append(curr_count)
                elif count_c or tmp_count:
                    time += 1
            for c in tmp_count:
                heapq.heappush(count_c, c)

        return time


if __name__ == '__main__':
    result = Solution().leastInterval2(tasks=["A", "A", "A", "B", "B", "B"], n=2)
    assert result == 8, f"Wrong result {result}"

    result = Solution().leastInterval2(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n=2)
    assert result == 12, f"Wrong result {result}"

    result = Solution().leastInterval2(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
    assert result == 16, f"Wrong result {result}"
