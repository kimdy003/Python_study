"""
    퀵 정렬
    Best: O(N logN), Avg: O(N logN), Worst: O(N logN)
"""


def quickSort(array, start, end):
    if start >= end:  # 원소가 1개인 경우
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pibot 보다 작은 데이터를 찾을 때까지 반복
        while start < right and array[pivot] <= array[right]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)


if __name__ == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    quickSort(array, 0, len(array) - 1)
    print(array)
