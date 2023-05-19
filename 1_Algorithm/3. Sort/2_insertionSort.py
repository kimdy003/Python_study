"""
    삽입 정렬
    Best: O(N), Avg: O(N^2), Worst: O(N^2)
"""


def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # 인덱스 i부터 1식 감소하며 반복하는 문법
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

            else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
        # print(array)


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    insertionSort(array)
    print(array)
