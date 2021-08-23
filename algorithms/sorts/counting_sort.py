def counting_sort(arr: list) -> list:
    arr = list(arr)
    cnt = [0 for i in range(max(arr) + 1)]

    for element in arr:
        cnt[element] += 1

    pos = 0
    for num in range(len(cnt)):
        for i in range(cnt[num]):
            arr[pos] = num
            pos += 1
    return arr
