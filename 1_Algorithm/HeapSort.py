def heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1  # 인덱스를 0부터 사용하기 때문에 +1, +2를 사용
    right_index = 2 * index + 2

    # 자식 노드와 값 비교
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    # 힙을 재정비
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)  # 하향식 힙 구조


def heap_sort(arr):
    length = len(arr)

    # 전체 원소에 대해 힙 구조 만들기
    for i in range(length // 2 - 1, -1, -1):  # 전체 개수의 반만 해줘도 된다
        heapify(arr, i, length)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 루트 노드와 맨 마지막 노드와 swap
        heapify(arr, 0, i)  # 힙 사이즈를 줄여주면서 원소의 위치를 지정한다

    return arr


import random

lst = [random.randint(1, 20) for i in range(20)]
sorted_list = heap_sort(lst)
sorted_list
