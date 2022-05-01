"""
21.10.15
1655_가운데로 말해요
"""

import sys
import heapq

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    number = int(input())
    heapq.heappush(arr, number)

    idx = len(arr) // 2
    if len(arr) % 2 == 0:
        idx -= 1
    print(arr[idx])
