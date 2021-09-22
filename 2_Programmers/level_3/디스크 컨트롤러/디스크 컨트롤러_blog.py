import heapq
from collections import deque

def solution(jobs):
    N, IDX = len(jobs), 0
    jobs.sort()
    jobs = deque(jobs)
    end, curr_time, waits, cand = 0, 0, 0, []

    #일을 다 할 때까지
    while end < N:
        #요청이 들어온 것이 없을 때
        if not cand:
            request, time = jobs.popleft()
            curr_time = request + time
            waits += time

        #요청이 들어온 것이 있을 때
        else:
            time, request = heapq.heappop(cand)
            curr_time += time
            waits += curr_time - request
        
        end += 1

        while jobs and jobs[0][IDX] <= curr_time:
            heapq.heappush(cand, jobs.popleft()[::-1])
    
    return waits // N


print(solution([[0, 3], [1, 9], [2, 6]]))