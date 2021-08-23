def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(arr: list, index: int, size: int):
    l = left(index)
    r = right(index)
    if l < size and arr[l] > arr[index]:
        largest = l
    else:
        largest = index
    if r < size and arr[r] > arr[largest]:
        largest = r
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, largest, size)


def build_max_heap(arr: list):
    length = len(arr)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(arr, index=start, size=length)
        start = start - 1


def heap_sort(arr: list):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, index=0, size=i)
    return arr
