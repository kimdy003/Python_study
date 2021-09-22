arr = [1, 1, 2, 4, 4, 5, 7, 7, 7, 10, 12, 12]
ssr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def upper(start, end):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] <= 7:
            start = mid + 1
        else:
            end = mid
    return arr[end]


def lower(start, end):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < 7:
            start = mid + 1
        else:
            end = mid
    return arr[end]


print(upper(0, len(arr) - 1))
print(lower(0, len(arr) - 1))
