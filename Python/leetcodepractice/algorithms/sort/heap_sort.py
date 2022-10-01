import math


def left(i: int) -> int:
    return i * 2 + 1


def right(i: int) -> int:
    return i * 2 + 2


def parent(i: int) -> int:
    return i // 2


def max_heapify(a: list[int], heap_size: int, i: int) -> None:
    lft = left(i)
    rit = right(i)
    largest = i
    if lft < heap_size and a[largest] < a[lft]:
        largest = lft
    if rit < heap_size and a[largest] < a[rit]:
        largest = rit
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a: list[int]):
    heap_size = len(a)
    for i in reversed(range(heap_size // 2)):
        max_heapify(a, heap_size, i)


def heap_sort(a: list[int]):
    build_max_heap(a)
    heap_size = len(a)
    while heap_size > 1:
        a[0], a[heap_size - 1] = a[heap_size - 1], a[0]
        heap_size -= 1
        max_heapify(a, heap_size, 0)


def heap_maximum(a: list[int]) -> int:
    return a[0]


def heap_extract_max(a: list[int]) -> int:
    max_ = a[0]
    a[0] = a[len(a) - 1]
    a.pop()
    max_heapify(a, len(a), 0)
    return max_


def max_increase_key(a: list[int], i: int, key: int):
    a[i] = key
    while i > 0 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


def max_heap_insert(a: list[int], key: int):
    # noinspection PyTypeChecker
    a.append(-math.inf)
    max_increase_key(a, len(a) - 1, key)


if __name__ == '__main__':
    a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    max_heapify(a, len(a), 1)
    heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    expected = heap
    assert a == expected, f"Expected {expected}, but {a}"

    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(a)
    expected = heap
    assert a == expected, f"Expected {expected}, but {a}"

    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_sort(a)
    expected = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    assert a == expected, f"Expected {expected}, but {a}"

    max_ = heap_extract_max(heap)
    assert max_ == 16, f"Expected {16}, but {max_}"
    expected = [14, 8, 10, 4, 7, 9, 3, 2, 1]
    assert heap == expected, f"Expected {expected}, but {heap}"

    max_increase_key(heap, 3, 100)
    expected = [100, 14, 10, 8, 7, 9, 3, 2, 1]
    assert heap == expected, f"Expected {expected}, but {heap}"

    max_heap_insert(heap, 1000)
    expected = [1000, 100, 14, 8, 10, 9, 3, 2, 1, 7]
    assert heap == expected, f"Expected {expected}, but {heap}"
