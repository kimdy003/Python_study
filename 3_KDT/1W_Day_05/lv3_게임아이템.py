#
#  lv3_게임아이템.py
#  게임아이템
#
#  Create by 김도영 on 2021/04/23
#


import heapq
from collections import deque

"""
그냥 list로 선언을 하여 pop(0)을 하면 
제거 후 앞으로 댕기는 작업이 있으므로 O(N) 시간이 걸린다.

하지만 deque로 선언을 하면 O(1) 시간만 걸린다.
"""


def solution(healths, items):
    answer = []
    healths.sort()
    items = deque(sorted([(item[1], item[0], index + 1) for index, item in enumerate(items)]))
    heap = []

    for health in healths:
        while items:
            debuff, buff, index = items[0]

            if health - debuff < 100:
                break
            items.popleft()
            heapq.heappush(heap, (-buff, index))

        if heap:
            _, index = heapq.heappop(heap)
            answer.append(index)

    return sorted(answer)


print(solution([200, 120, 150], [[30, 100], [500, 30], [100, 400]]))
