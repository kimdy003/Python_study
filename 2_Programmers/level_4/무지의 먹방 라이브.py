import heapq


def solution(food_times, k):
    answer, pq = [], []
    for i in range(len(food_times)):
        heapq.heappush(pq, [food_times[i], i + 1])

    pre_food = 0
    time = 0
    while True:
        if not pq:
            return -1

        length = len(pq)
        time += (pq[0][0] - pre_food) * length

        if time > k:
            time -= (pq[0][0] - pre_food) * length
            while pq:
                answer.append(heapq.heappop(pq)[1])
            answer.sort()
            return answer[(k - time) % length]

        else:
            pre_food = heapq.heappop(pq)[0]
