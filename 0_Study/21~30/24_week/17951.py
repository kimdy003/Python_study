import sys

input = sys.stdin.readline

N, K = map(int, input().split())
paper = list(map(int, input().split()))

answer = 0
left, right = 0, 10 ** 5 * 20 + 1
while left <= right:
    mid = (left + right) // 2

    group, score = 0, 0
    for s in paper:
        score += s
        if score >= mid:
            group += 1
            score = 0

    if group >= K:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
