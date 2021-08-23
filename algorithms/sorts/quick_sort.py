def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    temp = arr[0]
    left = [x for x in arr[1:] if x < temp]
    right = [y for y in arr[1:] if y >= temp]
    return quick_sort(left) + [temp] + quick_sort(right)
