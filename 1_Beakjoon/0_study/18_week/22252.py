import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
dic = defaultdict(list)

ans = 0
for _ in range(N):
    _input = input().split()
    if _input[0] == "1":
        for num in _input[3:]:
            heapq.heappush(dic[_input[1]], -int(num))
    else:
        if _input[1] not in dic:
            continue

        for _ in range(min(int(_input[2]), len(dic[_input[1]]))):
            ans += -heapq.heappop(dic[_input[1]])

print(ans)
