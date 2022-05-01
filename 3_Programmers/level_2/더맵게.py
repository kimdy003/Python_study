#더 맵게
import heapq

def solution(scoville, K):
    data = []
    for i in scoville:
        heapq.heappush(data, i)
    
    cnt = 0
    while data[0] < K:
        try:
            heapq.heappush(data, heapq.heappop(data)+heapq.heappop(data)*2)
        except IndexError:
            return -1
        cnt+=1
    
    return cnt
    

s = [1,2,3,9,10,12]
k = 7
solution(s, k)