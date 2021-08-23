def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    first = merge_sort(arr[:middle])
    second = merge_sort(arr[middle:])
    return merge(first, second)
