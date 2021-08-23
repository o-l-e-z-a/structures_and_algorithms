def bubble_sort(arr: list) -> list:
    arr = list(arr)
    for j in range(len(arr)):
        for j in range(len(arr)-1-j):
            if arr[j] > arr[j+1]:
                arr[j],  arr[j + 1] = arr[j+1],  arr[j]
    return arr
