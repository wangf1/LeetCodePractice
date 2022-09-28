def insertion_sort(a: list[int]):
    n = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            n += 1
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key

    print(n)


if __name__ == '__main__':
    input0 = [5, 4, 3, 2, 1, 100, -100, -99, 105, 6, 7, 5, 5, 5, 1, 1]
    insertion_sort(input0)
    print(input0)
    expected = [-100, -99, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 100, 105]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    input0 = [5, 4, 3, 2, 1, 100, -100, -99, 105, 6, 5, 5, 5, 1, 1]
    insertion_sort(input0)
    print(input0)
    expected = [-100, -99, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 100, 105]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    # test edge condition
    input0 = [1]
    insertion_sort(input0)
    print(input0)
    expected = [1]
    assert input0 == expected, f"Result should be {expected}, but {input0}"

    input0 = []
    insertion_sort(input0)
    print(input0)
    expected = []
    assert input0 == expected, f"Result should be {expected}, but {input0}"
