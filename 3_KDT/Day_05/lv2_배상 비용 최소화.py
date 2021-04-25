#
#  lv_배상 비용 최소화.py
#  배상 비용 최소화
#
#  Create by 김도영 on 2021/04/23
#


import heapq


def solution(no, works):
    result = 0
    hq = []

    for w in works:
        heapq.heappush(hq, -w)

    while no and hq:
        temp = heapq.heappop(hq)
        if temp != 0:
            temp += 1
            heapq.heappush(hq, temp)
        no -= 1

    for h in hq:
        result += h ** 2
    return result