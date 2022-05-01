import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = []


def lower_bound(ans, l):
    start, end = 0, len(ans)

    while start < end:
        mid = (start + end) // 2
        if ans[mid] < l:
            end = mid
        elif ans[mid] > l:
            start = mid + 1
        else:
            return mid
    return start


for l in lst:
    if not ans:
        ans.append(l)

    else:
        if ans[-1] > l:
            ans.append(l)
        else:
            pos = lower_bound(ans, l)
            ans[pos] = l
print(len(ans))
