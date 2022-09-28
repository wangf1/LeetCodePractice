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


# TODO implement other 6 functions and min-heap functions


if __name__ == '__main__':
    a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    max_heapify(a, len(a), 1)
    expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    assert a == expected, f"Expected {expected}, but {a}"
