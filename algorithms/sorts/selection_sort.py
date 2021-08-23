def find_min(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_array = []
    arr = list(arr)
    for i in range(len(arr)):
        smallest = find_min(arr)
        new_array.append(arr.pop(smallest))
    return new_array

