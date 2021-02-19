import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for _ in range(n):
        m = heapq.heappop(works)
        if m >= 0:
            heapq.heappush(works, m)
            break
        m += 1
        heapq.heappush(works, m)


    return sum(map(lambda x : (x*-1)**2, works))

print(solution(3, [1,1]))