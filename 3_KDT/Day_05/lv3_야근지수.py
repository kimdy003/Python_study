#
#  lv3_야근지수.py
#  야근지수
#
#  Create by 김도영 on 2021/04/23
#


from heapq import heapify, heappush, heappop


def solution(n, works):
    heap = []
    for work in works:
        heappush(heap, -work)

    while heap and n > 0:
        temp = heappop(heap)
        if temp == 0:
            continue

        temp += 1
        heappush(heap, temp)
        n -= 1

    return sum([work ** 2 for work in heap]) if heap else 0


print(solution([4, 3, 3], 4))