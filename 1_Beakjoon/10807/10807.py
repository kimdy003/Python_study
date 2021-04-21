from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
pivot = int(input())

print(count_by_range(arr, pivot, pivot))


