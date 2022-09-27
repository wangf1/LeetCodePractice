import math


class MergeSort:
    """
    Merge Sort - MIT <Introductions to Algorithms Second Edition Chinese Version> page 17 ~ 19
    """

    def sort(self, a: list[int], p: int, r: int) -> None:
        """
        Sort list[int] in ascending order with merge sort algorithm.
        :param a: the list[int] to be sorted
        :param p: the start index inclusive
        :param r: the end index exclusive
        :return: None. the a is sorted in place.
        """
        if p >= r - 1:  # Notice the boundary condition. r is exclusive end index.
            return
        q = (p + r) // 2
        self.sort(a, p, q)
        self.sort(a, q, r)
        self._merge(a, p, q, r)

    @staticmethod
    def _merge(a: list[int], p: int, q: int, r: int):
        left = []
        right = []

        for i in range(p, q):
            left.append(a[i])
        left.append(math.inf)  # infinite as sentinel

        for i in range(q, r):
            right.append(a[i])
        right.append(math.inf)

        i = j = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
 
    # Bottom up approach
    def sort2(self, a: list[int], p: int, r: int) -> None:
        size = 2
        while size // 2 <= r - p:  # Notice edge condition, make sure last time merge cover full list
            for i in range(p, r, size):
                self._merge(a, i, (i + i + size) // 2, min(i + size, r - p))
            size *= 2


if __name__ == '__main__':
    input0 = [5, 4, 3, 2, 1, 100, -100, -99, 105, 6, 7, 5, 5, 5, 1, 1]
    MergeSort().sort2(input0, 0, len(input0))
    print(input0)
    expected = [-100, -99, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 100, 105]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    input0 = [5, 4, 3, 2, 1, 100, -100, -99, 105, 6, 5, 5, 5, 1, 1]
    MergeSort().sort2(input0, 0, len(input0))
    print(input0)
    expected = [-100, -99, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 100, 105]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    # test edge condition
    input0 = [1]
    MergeSort().sort2(input0, 0, len(input0))
    print(input0)
    expected = [1]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    input0 = []
    MergeSort().sort2(input0, 0, len(input0))
    print(input0)
    expected = []
    assert input0 == expected, f"Result should be {expected}, but {input0}"
