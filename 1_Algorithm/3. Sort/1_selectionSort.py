"""
    선택 정렬
    Best: O(N^2), Avg: O(N^2), Worst: O(N^2)
"""


def selectionSort(array):
    for i in range(len(array)):
        minIdx = i  # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j

        array[i], array[minIdx] = array[minIdx], array[i]


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    selectionSort(array)
    print(array)
