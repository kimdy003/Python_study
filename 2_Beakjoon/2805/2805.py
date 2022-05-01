#
#  2805.py
#  나무 자르기
#
#  Create by 김도영 on 2021/04/23
#


from sys import stdin


n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2

    total = sum([l - mid for l in lst if mid < l])

    if total < m:
        end = mid - 1
    elif total > m:
        start = mid + 1
    else:
        end = mid
        break

print(end)
