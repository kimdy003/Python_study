import sys


input = sys.stdin.readline

N, C = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

left_lst = lst[: N // 2]
right_lst = lst[N // 2 :]

left_sum, right_sum = [], []


def brute_force(cur_lst, cur_sum, idx, w):
    if idx >= len(cur_lst):
        cur_sum.append(w)
        return
    brute_force(cur_lst, cur_sum, idx + 1, w)
    brute_force(cur_lst, cur_sum, idx + 1, w + cur_lst[idx])


def binary_search(arr, target):
    start, end = 0, len(arr)

    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


brute_force(left_lst, left_sum, 0, 0)
brute_force(right_lst, right_sum, 0, 0)
right_sum.sort()

cnt = 0
for i in left_sum:
    if C - i >= 0:
        cnt += binary_search(right_sum, C - i)

print(cnt)