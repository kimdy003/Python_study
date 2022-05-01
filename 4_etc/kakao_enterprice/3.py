# 21.07.05
import heapq


def segment(x, space):
    idx, ans = 0, 0
    while idx <= len(space) - x:
        temp = space[idx : idx + x]
        heapq.heapify(temp)
        ans = max(ans, temp[0])
        idx += 1

    return ans


print(segment(3, [2, 5, 4, 6, 8]))
