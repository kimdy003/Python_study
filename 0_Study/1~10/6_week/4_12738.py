import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


def lower_bound(ans, num):
    start, end = 0, len(ans) - 1
    while start < end:
        mid = (start + end) // 2

        if ans[mid] < num:
            start = mid + 1
        else:
            end = mid
    return start


ans = [arr[0]]
for num in arr[1:]:
    if num > ans[-1]:
        ans.append(num)
    else:
        idx = lower_bound(ans, num)
        ans[idx] = num

print(len(ans))
