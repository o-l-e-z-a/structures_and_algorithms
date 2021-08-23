def binary_search(array, item):
    low = 0
    high = len(sorted(array)) - 1

    while low <= high:
        middle = int((high + low) / 2)
        temp = array[middle]
        if temp == item:
            return middle
        elif temp > item:
            high = middle - 1
        else:
            low = middle + 1

    return None

