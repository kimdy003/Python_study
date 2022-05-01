import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
answer, Min = [], 2e9

lst.sort()
left, right = 0, N - 1
while left != right:
    temp = lst[left] + lst[right]
    if abs(temp) < Min:
        if temp == 0:
            answer = [lst[left], lst[right]]
            break
        answer = [lst[left], lst[right]]
        Min = abs(temp)

    if temp < 0:
        left += 1
    else:
        right -= 1

print(*answer)
