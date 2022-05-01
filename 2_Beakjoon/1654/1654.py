#
# 랜선 자르기
#

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
line = [int(input()) for _ in range(N)]


def Search(start, end):
    while start <= end:  # 등호가 없었다면 upper가 되어 K가 되는 수를 초과 하는 수 중 제일 작은 수가 반환
        mid_line = (start + end) // 2

        cnt = 0
        for l in line:
            cnt += l // mid_line

        if cnt >= K:
            start = mid_line + 1
        elif cnt < K:
            # 하지만 start와 end가 같아도 진행을 하여 upper에서 하나 작은 수를 반환 즉, K에 맞춘 제일 큰 수
            end = mid_line - 1
    return end


print(Search(1, max(line)))
