def binary_search(start, end, arr, no):
    if start > end:
        return -1

    mid = start + ((end - start) // 2)

    if arr[mid] == no:
        return mid

    elif arr[mid] > no:
        binary_search(start, mid - 1, arr, no)

    else:
        binary_search(mid + 1, end, arr, no)


arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

no = 6

x = binary_search(0, len(arr_sorted), arr_sorted, no)
print(x)
