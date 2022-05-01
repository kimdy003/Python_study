import sys


input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 1e9

left, right = 0, 1
sum = arr[0]
while left != N:
    if S <= sum:
        answer = min(answer, right - left)
        sum -= arr[left]
        left += 1
    else:
        if right == N:
            break
        sum += arr[right]
        right += 1

print(0 if answer == 1e9 else answer)
